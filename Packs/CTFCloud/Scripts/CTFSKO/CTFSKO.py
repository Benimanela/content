import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401

import traceback
import random

'''
           *//////
         ,////////*.                   ..,..              ,,,.
        //////     /////          .&&&&@@@@@&&(      /&&&&@@@&&&&&.      @&&@@@@@@&&&&     @@@@@&&&&@@@@@/    ,@&&@@@@@@@@@     ,@&&&    %&&@*
       /////,      //////.       &&&@.              @&&&,      #&&&(     @&&(      &&&#         /&&&          ,@&&.                &&&@&&&&
       /////       //////*       &&&/              .@&&&       .@&&%     @&&&@@@&&&&@(          /&&&          ,@&&&&&&&&@           (&&&&#
       ,/////      //////        *@&&%,      **     (@&&&,    /&&&@.     @&&(  .%&&&.           /&&&          ,@&&.               &&&@,*@&&&.
        ,//////.   ///,            .%@&&&&&&&@(       ,@@&&&&&&@%.       @&&(     #&&@/         /&&&          ,@&&&&&&&&&&@    ,&&&&.    .&&&@*
          *///////*
             ,/////
                                   .,,,,,,              ,,,,,,.           .,*//(///*,.                   .,*//(///*,.                     .,,,,,,,,.               ,,,,,,,,,,,,,,,,.
                                     /(((((/          /(((((*         ./(((((((((((((((((*           /(((((((((((((((((/,                ,((((((((((,              /((((((((((((((((((((,
                                       ((((((/      ((((((/          /((((((*.    ./(((((*        .((((((((*.    ./(((((((*              ((((((((((((.             /((((/////////(((((((((
                                         /(((((/  /(((((*           ,(((((,              ,       *(((((/             ,((((((           .(((((,  *(((((.            /((((/           ,(((((*
                                           /((((((((((*              (((((((/*,,.               .(((((*               .(((((*         .(((((,    ,(((((.           /((((/           .(((((*
                                             ((((((((                 ,((((((((((((((((/.       ,(((((,                /(((((        .(((((*      /(((((           /((((/          ,((((((.
                                           /((((((((((*                     ,/((((((((((((/     ,(((((,                (((((/       .(((((//////////(((((.         /((((((((((((((((((((/
                                         *(((((/  /(((((*                            /(((((.     ((((((.              /(((((.      .((((((((((((((((((((((.        /(((((((((((((((((,
                                       /(((((/      ((((((*         ,((/*.          ./(((((       /((((((*         ./((((((.       (((((*............/(((((        /((((/       .((((((.
                                     /(((((/         .((((((*       ,(((((((((((((((((((((          /((((((((((((((((((((,        (((((*              /((((/       /((((/         .(((((/
                                   ((((((/              ((((((/        /(((((((((((((((.               ,(((((((((((((/          .(((((*                /(((((      /((((/           *((((((


                                  ,*** .*  *,   ***,  ,*,  *,    */*     .**  .*  ,****  */*    .*  * .***, **** *. *, *. ,//.  ***. ,* ,* .*/,
                                  */,/*  /(     (((( ,/,/* /*   (  ,(    (*/* ,/    (.  (. */   ,(*(/ .(**   **   (**(*/ **  /,.(((* *///   */(
'''


good_images = [
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/deadpool-clapping.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/friends-joey.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/quality-quality-work.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/the-rock-dwayne-johnson.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/you-you-are.gif",
    "https://raw.githubusercontent.com/demisto/content/bf616e06fad91e5b1f32080eaf5ad8b6cfd29c1b/Packs/CTFCloud/doc_files/dancing-unicorn-unicorn.gif",
    "https://raw.githubusercontent.com/demisto/content/bf616e06fad91e5b1f32080eaf5ad8b6cfd29c1b/Packs/CTFCloud/doc_files/despicable-me-minions.gif"
]

bad_images = [
    "https://raw.githubusercontent.com/demisto/content/bf616e06fad91e5b1f32080eaf5ad8b6cfd29c1b/Packs/CTFCloud/doc_files/absolutely-not-nope.gif",
    "https://raw.githubusercontent.com/demisto/content/bf616e06fad91e5b1f32080eaf5ad8b6cfd29c1b/Packs/CTFCloud/doc_files/barackobama-talks.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/lion-king.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/robert-downey-jr-maybe.gif",
    "https://raw.githubusercontent.com/demisto/content/ctf/Packs/ctf01/doc_files/the-rock-look-the-rock-meme.gif"
]

HTML_MESSAGE_1 = '''
<img src="%s" alt="Robot">
<div style='font-size:18px;'>
Well Done!!!
</div>
''' % (good_images[random.randint(0, len(good_images) - 1)])

HTML_MESSAGE_BAD = '''
<img src="%s" alt="Error">
<div style='font-size:18px;'>
Nope!!! Try again.
Remember to overwrite the "secret" argument when you are re-running the task.
To re-run this task -> Click on "Complete Task" -> clear the Secret value using the trash-can icon -> fill out the Secret value -> click on the 'Run script now' :)
</div>
''' % (bad_images[random.randint(0, len(bad_images) - 1)])

answers = {
    "01": ["ip address", "ip", "address"],
    "02": ["virustotal"],
    "03": ["192.42.116.193"],
    "04": ["aws", "amazon"],
    "05": ["666688938958"],
    "06": ["akiazvsi4536365ad6wcjc"],
    "07": ["create user", "createuser", "user creation", "addusertogroup", "add user to group"],
    "08": ["4331"],
    "09": ["noneofyourbusiness.io", " noneofyourbusiness.io"],
    "10": ["detected"],
    "11": ["xdr agent is not installed", "xdr agent is not communicating with the xdr server"],
    "12": ["true positive"],
    "13": ["keepcalmandstaysecure"],
    "14": ["ctf cloud use case"],
    "15": ["hastalavistababy", "hasta lavista baby", "hasta la vista baby", "hast alavi stababy"]


}

# MAIN FUNCTION #


def main():
    try:
        args = demisto.args()
        # __Error handeling when there is an empty secret or question id__
        if (args.get("secret") == None or args.get("question_ID") == None):
            return_error(f'Please specify Secret and Question ID to proceed with the challange')

        if (args.get("secret").lower() in answers[args.get("question_ID")]):
            return_results({
                'ContentsFormat': EntryFormat.HTML,
                'Type': EntryType.NOTE,
                'Contents': HTML_MESSAGE_1,
            })
        # General Error handeling
        else:
            # if (args.get("question_ID") ==  "03"):
            #    return_error(f'In case the playbook is in "Quite Mode", no output will be displayed in the war-room.\n\nYou can skip this task if you want or re-run it with <none> :). ')
           # else:
            #return_error(f'Nope... try again!!!\nRemember to overwrite the "secret" argument when you are re-running the task :)')
            demisto.results({
                'Type': entryTypes['error'],
                'ContentsFormat': formats['html'],
                'Contents': HTML_MESSAGE_BAD,
            })

    except Exception as exc:  # pylint: disable=W0703
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute this script. Error: {str(exc)}')


# ENTRY POINT #


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
