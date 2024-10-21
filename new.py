#PIL：是一种图像处理库，使用前需要先使用pip install pillow进行下载
#Python版本：3.6.x

from PIL import Image

#定义输出图像的大小
width=800
height=200

#记录ascii字符，字符画由这些字符组成
ascii_list= list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将图像中每个像素点的RGB值映射为灰度值
#在opencv中，标准转换公式为：灰度值=0.2989×R+0.5870×G+0.1140×B
#alpha是透明度，0是彻底透明
def transfer(R,G,B,alpha=256):
    if alpha==0:    #透明度为0，返回空字符
        return ""
    char_len=len(ascii_list)    #计算ascii_list的长度
    # 将图像中单个像素的RGB值转换灰度
    gray=int(0.2989*R+0.5870*G+0.1140*B)
    #计算每个像素的灰度值在ascii_list中间隔（重点）
    # 灰度值的区间为[0~255]，这里+1是为了分配字符的时候能够覆盖到最大的灰度值，即255
    # 无法理解unit的话，我这里举个例子，在ascii_list中第一个元素为'$'，第二个元素为'@',
    # 这里是用灰度总体值除以ascii_list的长度，所以如果unit是4,那'$'和'@'之间的间隔为4，
    # 也就是说在'@'之前全是'$'，'$''$''$''$''@'
    unit=(256+1)/char_len
    return ascii_list[int(gray/unit)]   #int(gary/unit)就能判断是在ascii_list中是哪一个字符

if __name__=="__main__":
    # 输入
    img=Image.open('test.jpg')
    # 调整初始图像的大小，使用Image中的最近邻插值法进行扩大和缩小，也就是NEAREST
    img=img.resize((width,height),Image.NEAREST)
    # 初始化用于存储字符画的字符串
    output=""
    for i in range(height):
        for j in range(width):
            output+=transfer(*img.getpixel((j,i))) #获取图像中所有像素的RGB值以及alpha值
        output+='\n'#输入完每一行字符进行换行
    print(output)
    #sava
    with open("output.txt","w") as file:
        file.write(output)
