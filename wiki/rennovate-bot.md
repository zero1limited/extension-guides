# Rennovate Bot

## Initial setup
This is required on a per organisation basis. You will also need a candidate repository to install on first.
1. Create a Github App
  Follow instructions from here: https://docs.renovatebot.com/modules/platform/github/#running-as-a-github-app for _Organisation_
2. Make a note of **App ID**
3. Click "Generate a new client secret", copy the value and make a note of it.
4. Scroll to the bottom of the page and click "Generate a private key", it will automatically create and download.
5. Navigate to "Install App".
    Click Install
    Select "Only select repositories"
    Pick a repository
    Click Install
   In the url would will see `/installations/INSTALLATION_ID`, make a note of your installation ID.
6. Naviate to Security > Secrets and Variables > Actions
  (It should be in the left hand nav)
7. For each of the bits of information we created we want create a secret.
  **App ID** -> `RENOVATE_APP_ID`
  **INSTALLATION_ID** -> `RENOVATE_INSTALL_ID`
  **Private Key** -> `RENOVATE_PRIVATE_KEY`
  The repository access field is up to you. If all your Magento repositories are private, you should be good to leave at "Private repositories"


App ID: 414026
Client Secret: f1974c64f70932fc01a391865701db2a9e8f8775
INSTALLATION_ID: 43316951
Private Key:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0DriAvmNhTc7dSlyCUNGyValG9dJoKgijJSmDvqI1lzvndad
9SaEdFgaJDf8XmsN5/aDguKpocfmx3BQcIYzettEgVC1DFcD/HyCFqHIilh206aA
3EGghiRekVHnyD08SnLkfHnRVT0k7WoCCPPlyaUfhsx2xx+WEIANQlK5o5/vAmgz
g0DaaiMD8zNW9taVHF5T3q30Y0JdIHCCQpEI38OyTFy722J2Z0Cti0My6jyvPeti
SJVDn1mOFLLm9OjANe4CGXqNQEgnKr425dcd8pVbR9bAywJTPwegBhGXjq3PuGKx
iPCvlafVwFtFt7+AU3iP1JdQjZA59uX/2IJ1GwIDAQABAoIBAQCPiYdydYPQaJpb
0Q4CxJVvBIMcBfODA2ONdIpjmN/qpHWoX+DStJJpgLHEdbNJgpI7a/qLpqM4GgxD
PnC0oE2sSqmWWoPy1aixy0IBR9RtST3f986sBbEZxshJdCRKK6v7xecqxu49y8BA
x+pPMZEcxu5MhXT7HhLbnOmG5m+BEefUhlf47ceUHgIuEZppCCjsEjmbJwRnSt6u
krflYn+FoP3DpdZZO48csOUe4wkyjhCmMXmblGjdFstbKIxATiPwHCoC5kVME4Ij
rB25+PKcPzwBGcCtMNzeJa82079pU2Iq5cYPf0xryLhjZnbcfLd3Hp6Oibf57DZ5
fZxvTesBAoGBAOwPzPgMwUnXI/aUVrJ3cYg1WDgJtH4sBFuE18xedpvYXzp1ELVZ
o3hu67+WPn8jU0hRltlWxloduATfNmK5+C0+1ADfRb/BZV3Yiw+kIvm9WiQUCmVC
8Z9L4z6+2VtCJchSVZzIq7EnuKvkdNjpiQdSr+xvRJQXxWu13S9H6wlrAoGBAOHR
S99k4E3gnxcYHqVYE2SlC5t2IfKH2Y7cGT2TFAGKrR52N4XyBu9TaEbboWu1vAE3
HnPtJm0xTSrQGQ64XWWBXn39xlK36Ud9XhOXtZyKLSklnxq1zF+LOPn7czmM2B0r
Ka5nHOWGEWmHlfHX8HRyrFFbkyn3SYLsGd85oL8RAoGBAJJ947bzQ2ftaNX2jC7I
TN44LHzqGOZLrpCUyc57uKNSDRab2ziPXhC41PfZ5wLDC0XPzAsn/IOj+bScSIXP
3qFFYg8Af6pV++/XF8UnGMVeqnfFMAZTGtq+H1Gq4fvt+sBrx9E5/sI7YjDZ32FU
28J9n8rb6fT1I4CKJa7XtJXtAoGAdqP/uN7G+iOJchi6ASTFC5uq/YKTU1kMdIIu
wKsFV8oEKnzxru35tsObhZ7esDhLDlhnJ4DxL203nca3Y4R5jVrqykcKa2s0pNq5
EpIiWJxAHd4mOWJKfegnhy8U2qek465Jt9d01yIZA9i4bteE/alB33y9VM8XUDG7
Zgxg6AECgYEArqPiQZ59ZrVea+xmduQXm1bDK0WBmpCdIYV3Q0jPZMPIiFDW2dZ5
O3PIch8y09cuau5uJ4QBvma43l7fzFZiVnb41+gv2MB5irmrzWJObCIQzuGevznb
t/WfVgDfg/SS7ngAdJFdaRHH86rMTjUUVwPaA6CKe8rNcPwMJcZ5Ekw=
-----END RSA PRIVATE KEY-----

```


## Adding new reposiorties
Once you have installed the Github app, adding additional repositories is relatively simple.

1. In the `default` git branch for the repo you need the following files.
  - `.github/workflows/renovate.yml`
    ```yml
    name: Renovate
    on:
      # Allows manual/automated ad-hoc trigger
      workflow_dispatch:
        inputs:
          logLevel:
            description: "Override default log level"
            required: false
            default: "info"
            type: string
          overrideSchedule:
            description: "Override all schedules"
            required: false
            default: "false"
            type: string
      schedule:
        - cron: '30 4 * * *'

    jobs:
      call-workflow:
        uses: zero1limited/github-actions-magento/.github/workflows/renovate.yml@master
        with:
          logLevel: ${{ inputs.logLevel || 'info' }}
          overrideSchedule: ${{ github.event.inputs.overrideSchedule == 'true' && '{''schedule'':null}' || '' }}
        secrets: inherit
    ```
  - `renovate.json`
    ```yml
    {
      "$schema": "https://docs.renovatebot.com/renovate-schema.json",
      "extends": [
        "github>zero1limited/renovate-config:magento"
      ],
      "hostRules": [],
      "constraints": {
        "php":"8.1.16"
      }
    }
    ```
    If your composer credentials are stored in `auth.json` within your project you don't need to do anything else.  
    If your composer credentials aren't stored in `auth.json` within your project please see [Using Github Secrets](#using-github-secrets)  
    You also need to update the PHP version to the correct one for your project.

2. Navigate to your Apps (you should of previously create an app for renovate to run as)
  Go to "Install App".
  If you haven't installed for any repositories before:
    Click Install
    Select "Only select repositories"
    Pick a repository
    Click Install

3. You can then go to your project (in Github) > actions and you should see `Renovate`.
  You can manually trigger, or wait for cron.
  
### Using Github Secrets
For each credential set you need to add a secret username and password to github actions prefixed with `RENOVATE_SECRET_`.
For example if your `auth.json` looks like this
```json
{
    "http-basic": {
        "repo.magento.com": {
            "username": "thisisausername",
            "password": "thisisapassword"
        },
        "gitlab.anothervendor.com": {
            "username": "token",
            "password": "secretsecretsecret"
        },
    }
}
```

You would need to create (in Github) the secrets:
- `RENOVATE_SECRET_MAGENTO_USERNAME`: with value `thisisausername`
- `RENOVATE_SECRET_MAGENTO_PASSWORD`: with value `thisisapassword`
- `RENOVATE_SECRET_ANOTHERVENDOR_USERNAME`: with value `token`
- `RENOVATE_SECRET_ANOTHERVENDOR_PASSWORD`: with value `secretsecretsecret`

You would then need to add the following to the `hostRules` array within `renovate.json`
```
{
  "hostType": "packagist",
  "matchHost": "https://repo.magento.com",
  "username": "{{ secrets.MAGENTO_USERNAME }}",
  "password": "{{ secrets.MAGENTO_PASSWORD }}"
},
{
  "hostType": "packagist",
  "matchHost": "https://gitlab.anothervendor.com",
  "username": "{{ secrets.ANOTHERVENDOR_USERNAME }}",
  "password": "{{ secrets.ANOTHERVENDOR_PASSWORD }}"
}
```

The renovate workflow, will automatically find all Github secrets prefixed with `RENOVATE_SECRET_`. Remove this prefix and pass it to the renovate service, which will translate the credentials `renovate.json`. This way you are able to authenticate to multiple Composer repositories without need to commit credntials to source control.


### Acknowledgements
- https://medium.com/@superseb/maintenance-free-renovate-using-github-actions-workflows-d91d32ad854a
- Peter Jaap