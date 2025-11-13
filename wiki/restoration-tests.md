<!-- TITLE: Restoration Tests -->
<!-- SUBTITLE: A quick summary of Restoration Tests -->

# Restoration testing for ZERO-1 Clients
1. Create an instance for this task
2. Once the instance has finised creating open the setting dialog (for that instance **not the live connector**)
- Make sure Code > Backup is "latest" (if it isn't, change it to "latest")
- Make sure Mysql Backup is "lastest full" (if it isn't, change it to "latest full")
- Save **Without recreating modified components**
3. Recreate the instance (Sync Code + Mysql)
4. Carry out standard test plan
5. Delete instance

### If an Issue is Found
1. Provide detailed replication steps in the task and alert Suzanne.
2. Raise a new ticket for the issue in 2nd line in the support task list.
3. Inform the client your investigating an issue that been identified in the quarterly restoration testing task.
4. 2nd line to investigate the issue and verify if the issue would prevent successful restoration.
5. Implement a fix if required.
6. After the fix is released resync the restoration test instance with fresh backups and retest to ensure the issue is resolved and there are no further issues present.

<!-- old instructions
1. Login to Mdoq, find the live connector for the client.  
  Open the settings dialog:  
  - change code backup to the file. e.g backup-yyyy-mm-dd _not_ "latest"
    ![code-backup-select-snapshot.png](/code-backup-select-snapshot.png)
  - change mysql back to "latest sanitized"
2. Create an instance for this task.
3. Login to https://jenkins.mdoq.io/job/Misc/job/push-backup-to-mdoq/ using user backups-to-mdoq and request LastPass password from Arron
4. Obtain the SERVER code and INSTANCE_ID which  should be in the task description
5.Run a jenkins job for code ("BACKUP_TYPE" == "code-backup") and for db ("BACKUP_TYPE" == "full-db-backup")![](http://g.recordit.co/1Ys6xKkVn2.gif)
  One the Jenkins job reports completion you should then be able to visit MDOQ and see the code backup as illustrated below, if this is NOT the case you must immediately escalate this to your line manager.
  ![](http://g.recordit.co/Zpl4OipMWh.gif)
6. Edit your instance:
  - change code backup to "latest"
  - change mysql backup to "latest full"
7. Recreate your instance
8. Carry out standard test plan
9. delete instance
10. delete the code backup you pushed (sak > snapshots > code)
11. Edit the live instance:
  - change code backup to "latest"
  - change mysql backup to "latest sanitized"
-->
