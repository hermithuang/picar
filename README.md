# picar
首先是连线。需要使用一个L298N电机驱动板模块，接线包括:<br />

1、单侧电机并联。L298 两边的out各接一边电机的两个脚。注意要同侧电机方向运行方向相同。 <br />
2、L298输入接口，地线和12V线接电池盒，5V供电用树莓派，电池盒估计要高一点的电压，6V的电压勉强带起来，买了个9V的试试。 <br />
3、四个input输入接树莓派4个gpio口。<br />

然后就是控制的页面，使用web.py做了一个。 <br />
命令：<br />
pip install web.py <br />
./car.py 可以在 8080上起一个页面。<br />

然后就是如何获取图像。这里有几个点 <br />
1、用jwplayer，这种可以在PC上看到图像，但是android上看不到图像。不支持 <br />
2、用https://github.com/AndyA/psips，这种的话都可以看到图像，但电脑上需要加个插件，而且形式上是生成一个个ts文件，可以拉，单不是实时图像。 <br />
3、最终解决方法，用https://github.com/jacksonliam/mjpg-streamer，编译安装完了之后，用以下命令启动。这样在2222端口上?action=stream可以出现图像。 <br />

mjpg_streamer -o "output_http.so -w /root/git/mjpg-streamer/mjpg-streamer-experimental/www/ -p 2222" -i "input_raspicam.so -x 360 -y 240 -d 200 -fps 15 -q 50 -rot 180 <br />

最终访问IP：8080/static/index.html就可以看到最终的效果了。 <br />
