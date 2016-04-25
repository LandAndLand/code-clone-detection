
for file in `find ~/programs/project_dataset/aashish/ -name '*.py'`; do
  resfile=`echo $file|tr -d '/ -'`
  echo "python2 test.py ~/programs/project_dataset/aashish/ .py $file > $resfile"
  python2 test.py ~/programs/project_dataset/aashish/ .py $file > $resfile
done
