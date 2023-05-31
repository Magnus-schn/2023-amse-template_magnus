echo ~~~ Start Pipeline~~~
python ../data/data_pipeline.py
echo ~~~ Automated Test ~~~
python test.py
echo ~~~ Testing done. ~~~