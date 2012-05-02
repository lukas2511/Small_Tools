#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv ){
	if(argc!=2){
		printf("Usage: blight +/-/[1-15]\n");
		exit (1);
	}
	FILE *fp;
	char data[2];
	int value;
	int newvalue=-1;
	char newdata[2];
	fp = fopen("/sys/devices/virtual/backlight/apple_backlight/brightness","r");
	fgets(data,3,fp);
	fclose(fp);
	value = atoi(data);
	if(argv[1][0]=='+'){
		newvalue=value+1;
	}else if(argv[1][0]=='-'){
		newvalue=value-1;
	}else if(atoi(argv[1])>0 && atoi(argv[1])<16){
		newvalue=atoi(argv[1]);
	}

	if(newvalue!=-1){
		sprintf(newdata,"%d",newvalue);
		fp = fopen("/sys/devices/virtual/backlight/apple_backlight/brightness","w");
		fwrite(newdata,1,sizeof(newdata),fp);
		fclose(fp);
	}
}
