obj-m := imx219.o bcm2835-unicam.o bcm2835-isp.o 
bcm2835-isp-objs := bcm2835-v4l2-isp.o

obj-$(CONFIG_VIDEO_ISP_BCM2835) += bcm2835-isp.o

ccflags-y += \
    -I$(srctree)/drivers/staging/vc04_services \
    -D__VCCOREVER__=0x04000000
clean:
	rm -rf *.o *.mod *Module* *.ko .*
