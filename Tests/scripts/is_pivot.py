import gitlab
import os
from datetime import datetime, timedelta
from dateutil import parser



def get_pipelines_and_commits(gitlab_url:str, gitlab_access_token:str, project_id:str, look_back_hours:int):
    """
    Get all pipelines and commits on the master branch in the last X hours,
    pipelines are filtered to only include successful and failed pipelines.
    Args:
        gitlab_url - the url of the gitlab instance
        gitlab_access_token - the access token to use to authenticate with gitlab
        project_id - the id of the project to query
        look_back_hours - the number of hours to look back for commits and pipeline
    Return:
        a list of gitlab pipelines and a list of gitlab commits in ascending order
    """
    gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_access_token)
    project = gl.projects.get(project_id)

    # Calculate the timestamp for look_back_hours ago
    time_threshold = (
        datetime.utcnow() - timedelta(hours=look_back_hours)).isoformat()

    commits = project.commits.list(all=True, since=time_threshold, order_by='updated_at', sort='asc')
    pipelines = project.pipelines.list(all=True, updated_after=time_threshold, ref='master',
                                       source='push', order_by='updated_at', sort='asc')

    # Filter out pipelines that are not done
    filtered_pipelines = [
        pipeline for pipeline in pipelines if pipeline.status in ('success', 'failed')]

    return filtered_pipelines, commits


def shame(commit):
    """
    Returns the name, email, and PR link for the author of the provided commit.

    Args:
        commit: The Gitlab commit object containing author info.

    Returns:
        name: The name of the commit author.
        email: The email of the commit author.
        pr: The GitHub PR link for the Gitlab commit.
    """
    name = commit.author_name
    email = commit.author_email
    pr_number = commit.title.split()[-1][2:-1]
    pr = f"https://github.com/demisto/content/pull/{pr_number}"
    return name, email, pr


def are_pipelines_in_order_as_commits(commits, current_pipeline_sha, previous_pipeline_sha):
    """
    This function checks if the commit that triggered the current pipeline was pushed
    after the commit that triggered the the previous pipeline,
    to avoid rare condition that pipelines are not in the same order as their commits.
    Args:
        commits: list of gitlab commits
        current_pipeline_sha: string
        previous_pipeline_sha: string

    Returns:
        boolean , the commit that triggered the current pipeline
    """
    current_pipeline_commit_timestamp = None
    previous_pipeline_commit_timestamp = None
    for commit in commits:
        if commit.id == previous_pipeline_sha:
            previous_pipeline_commit_timestamp = parser.parse(commit.created_at)
        if commit.id == current_pipeline_sha:
            current_pipeline_commit_timestamp = parser.parse(commit.created_at)
    if not current_pipeline_commit_timestamp or not previous_pipeline_commit_timestamp:
        return False, None
    return current_pipeline_commit_timestamp > previous_pipeline_commit_timestamp, commit


def is_pivot(single_pipeline_id, list_of_pipelines, commits):
    """
    Check if a given pipeline is a pivot, i.e. if the previous pipeline was successful and the current pipeline failed and vise versa
   Args:
    single_pipeline_id: gitlab pipeline ID
    list_of_pipelines: list of gitlab pipelines
    commits: list of gitlab commits
    Return:
        boolean | None, gitlab commit object| None
    """
    current_pipeline = next((pipeline for pipeline in list_of_pipelines if pipeline.id == int(single_pipeline_id)), None)
    pipeline_index = list_of_pipelines.index(current_pipeline) if current_pipeline else 0
    if pipeline_index == 0:         # either current_pipeline is not in the list , or it is the first pipeline
        return None, None
    previous_pipeline = list_of_pipelines[pipeline_index - 1]

    # if previous pipeline was successful and current pipeline failed, and current pipeline was created after
    # previous pipeline (n), then it is a negative pivot
    in_order, pivot_commit = are_pipelines_in_order_as_commits(commits, current_pipeline.sha, previous_pipeline.sha)
    if in_order:
        if previous_pipeline.status == 'success' and current_pipeline.status == 'failed':
            return True, pivot_commit
        if previous_pipeline.status == 'failed' and current_pipeline.status == 'success':
            return False, pivot_commit
    return None, None

