# Ease_scheduler
[Easy_Scheduler official](http://easydata.ru/en/products/easyscheduler/)

[Easy_Scheduler source](http://easydata.ru/download/easyportal/])

## Instructions
```
yum install -y rpm-build rpm-devel rpmlint rpmdevtools

cd ~
rpmdev-setuptree
cd ~/rpmbuild/SOURCES/
wget http://easydata.ru/download/easyportal/scheduler-1.9.8.zip

cd ~/rpmbuild/SPECS
cp ~/easysheduler.spec easysheduler.spec
rpmbuild -ba easysheduler.spec

# show RPM
ls -l ~/rpmbuild/RPMS/x86_64/
easyscheduler-EasyScheduler-1.9.8-1.x86_64.rpm # Server
easyscheduler-EasyRuntime-1.9.8-1.x86_64.rpm   # Client

# don't forget about *.srpm
ls -l ~/rpmbuild/SRPMS/
```

## Notes
### 1. Delete libs exclude x86_64
#### error
```
ERROR   0002: file '/opt/easyportal/runtime/lib/sigar/libsigar-amd64-solaris.so' contains an invalid rpath '/usr/sfw/lib' in [/usr/sfw/lib]
error: Bad exit status from /var/tmp/rpm-tmp.fKNu5F (%install)
```

#### resolve
```
# remove lib for non x86_64 arch
for FILE in %{buildroot}/opt/easyportal/runtime/lib/sigar/*; do
  if ! echo "$FILE" | grep amd64-linux &>/dev/null ; then
    rm -f "$FILE"
  fi
done
```

### 2. Disable .jar rebuilb
[Fedora maillist](https://www.redhat.com/archives/fedora-devel-java-list/2008-September/msg00040.html)
```
# disable repack .jar
%define __jar_repack %{nil}
```

