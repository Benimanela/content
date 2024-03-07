## Redmine Integration

- Redmine is a flexible project management web application. Written using the Ruby on Rails framework, it is cross-platform and cross-database.
- Redmine is open source and released under the terms of the GNU General Public License v2 (GPL).

## Authentication:

1. Navigate to your server URL to access your account.
2. Enter your username and password.
3. Go to "My Account" located at the top right corner of the page.
4. Click on "API access key" and select "Show" to reveal your API key.
5. Input the API key into the Redmine integration authentication window.
 
## Configuring a Project ID

1. If you would like to display data related only to a project with id x- Fill it in the Redmine integration authentication window.
2. If you mention a Project ID in the command- it will override the configured Project ID.
3. You can leave the project ID blank (if not required).

## General noted

1. When using commands such as "update" or "create," certain fields may remain unchanged due to insufficient privileges. In such cases, while the command itself will not fail, those particular fields will not be updated.

### Your API key carries all your privileges, so keep it secure and don’t share it with anyone.
         