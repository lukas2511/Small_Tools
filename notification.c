#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;

void setled(int value){
	FILE *fp;
	fp = fopen("/sys/devices/platform/applesmc.768/leds/smc::kbd_backlight/brightness","w");
	if(value==0){
		fwrite("0",1,1,fp);
	}else if(value==255){
		fwrite("255",1,3,fp);
	}
	fclose(fp);
}

int main(int argc, char** argv ){
	int delay=100000;
	setled(255);
	usleep(delay);
	setled(0);
	usleep(delay);
	setled(255);
	usleep(delay);
	setled(0);
	usleep(delay);
	setled(255);
	usleep(delay);
	setled(0);
	usleep(delay);
}

