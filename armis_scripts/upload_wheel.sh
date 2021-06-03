#!/bin/bash

index_prefix="
<!DOCTYPE html>
<html>
<head>
    <title>Links</title>
</head>
<body>
"
index_suffix="
</body>
</html>
"

wheels_dir="./dist/"
packages=`(cd $wheels_dir; ls *.whl | cut -d "-" -f 1 | sort -u)`

for pkg in $packages; do
    cannonical_name=`echo $pkg | sed "s/[_.]/-/g" | tr "[:upper:]" "[:lower:]"`
    echo "Updating wheels for $cannonical_name package..."
    aws s3 sync $wheels_dir s3://armis-wheels/$cannonical_name/ --exclude="*" --include="$pkg-*.whl"
    links=`aws s3 ls s3://armis-wheels/$cannonical_name/ | grep "\.whl" | awk '{print "    <a href=\"" $4 "\">" $4 "</a><br/>"}'`
    echo "$index_prefix$links$index_suffix" | aws s3 cp --content-type="text/html" --cache-control="no-cache" - s3://armis-wheels/$cannonical_name/index.html
done

echo "Done updating all wheels."
