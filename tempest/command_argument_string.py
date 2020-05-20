from tempest import tvaultconf

#Workload commands
workload_list = "workloadmgr --insecure workload-list | grep available | wc -l"
workload_create = "workloadmgr --insecure workload-create --workload-type-id "+tvaultconf.workload_type_id+\
                  " --display-name "+tvaultconf.workload_name+\
                  " --source-platform "+tvaultconf.source_platform
workload_delete = "workloadmgr --insecure workload-delete "
workload_modify = "workloadmgr --insecure workload-modify "
workload_unlock = "workloadmgr --insecure workload-unlock "
workload_type_list = "workloadmgr --insecure workload-type-list | grep '[a-z0-9]-[a-z0-9]' | wc -l"
workload_type_show = "workloadmgr --insecure workload-type-show " + str(tvaultconf.workload_type_id)
workload_show = "workloadmgr --insecure workload-show "
workload_import = "workloadmgr --insecure workload-importworkloads"

get_storage_usage = "workloadmgr --insecure workload-get-storage-usage" 
get_import_workloads_list = "workloadmgr --insecure workload-get-importworkloads-list" 
workload_disable_global_job_scheduler = "workloadmgr --insecure disable-global-job-scheduler"
workload_enable_global_job_scheduler = "workloadmgr --insecure enable-global-job-scheduler"
get_nodes  = "workloadmgr --insecure workload-get-nodes" 
get_auditlog = "workloadmgr --insecure workload-get-auditlog"


#Snapshot commands
snapshot_list = "workloadmgr --insecure snapshot-list | grep available | wc -l"
snapshot_create = "workloadmgr --insecure workload-snapshot " + " --full --display-name " +tvaultconf.snapshot_name + " "
snapshot_delete = "workloadmgr --insecure snapshot-delete "
incr_snapshot_create = "workloadmgr --insecure workload-snapshot " + " --display-name " +tvaultconf.snapshot_name + " "
snapshot_cancel = "workloadmgr --insecure snapshot-cancel "

#Restore commands
restore_list = "workloadmgr --insecure restore-list | grep available | wc -l"
restore_delete = "workloadmgr --insecure restore-delete "
oneclick_restore = "workloadmgr --insecure snapshot-oneclick-restore --display-name " +tvaultconf.restore_name
selective_restore = "workloadmgr --insecure snapshot-selective-restore --display-name " +tvaultconf.selective_restore_name+ " --filename " +tvaultconf.restore_filename
restore_show = "workloadmgr --insecure restore-show "
inplace_restore = "workloadmgr --insecure snapshot-inplace-restore --display-name test_name_inplace --display-description test_description_inplace  --filename "
restore_cancel = "workloadmgr --insecure restore-cancel "

#Nova commands
delete_vm = "nova delete "
list_vm = "nova list | awk -F '|' '{print $2}' | grep -v ID"

#License commands
license_create = "workloadmgr --insecure license-create "
license_check = "workloadmgr --insecure license-check"
license_list = "workloadmgr --insecure license-list"

#Config backup commands
config_workload_configure = "workloadmgr --insecure config-workload-configure"
config_workload_show = "workloadmgr --insecure config-workload-show"
config_backup = "workloadmgr --insecure config-backup"
config_backup_show = "workloadmgr --insecure config-backup-show"
config_backup_delete = "workloadmgr --insecure config-backup-delete"

#Workload policy commands
policy_create = "workloadmgr --insecure policy-create --policy-fields "
policy_update = "workloadmgr --insecure policy-update --policy-fields "
policy_assign = "workloadmgr --insecure policy-assign --add_project "
policy_delete = "workloadmgr --insecure policy-delete "
