# rpmbuild
rpmbuild


## install rpmbuild

```
yum install rpmbuild
yum install rpmdevtools 
rpmdev-setuptree
```

## check rpmbuild topdir

```
rpmbuild --showrc | grep topdir 
```

## generate rpm package

```
cd SPECS/
rpmbuild -ba *.spec
```