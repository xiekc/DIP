# DIP homework 4

16327109 谢昆成

## 1. Exercises

### 1.1 Chromaticity Diagram

(1)
$$
aberration=\sqrt{(x_1-x2)^2+(y_1-y_2)^2}
$$
(2)

Suppose $x_1>x_2$, $y_1>y2$
$$
x_0=\frac{x_0-x_2}{x_1-x_2}x1+\frac{x_1-x_0}{x_1-x_2}x_2
$$

$$
y_0=\frac{y_0-y_2}{y_1-y_2}y1+\frac{y_1-y_0}{y_1-y_2}y_2
$$

$$
\therefore \ value_{0}=\frac{x_0-x_2}{x_1-x_2}value_1+\frac{x_1-x_0}{x_1-x_2}value_2
$$



### 1.2 Color Space

(1)

RGB consists of 3 color components: red, green and red, which decomposes a color into this three colors. It is more suitable to display and generate color.

HSI consists of 3 sense components: hue, saturation and intensity, which is more intuitive to explain the sight sense of humans.

(2)

A=(1,0,1), B=(0,0,1)

from RGB to HSI

B>G, A=(300,1,2/3)

B>G, B=(240,1,1/3)

then set the intensity to 1

A=(300,1,1)

B=(240,1,1)

convert them back to RGB

A is in BR sector, A=(3/2,0,3/2)

B is in BR sector, B=(0,0,3)

The new RGB values exceed 1 and so we have to normalize them to 1

A=(1,0,1)

B=(0,0,1)

in the end, it is the same with original RGB values



## 2. Programming Tasks

My student ID is 16327109, so I take "09.png" as my input.

### 2.1 Histogram Equalization on Color Images

1.

the original image

![](./img/09.png)

The RGB histograms

| R                      | G                      | B                      |
| ---------------------- | ---------------------- | ---------------------- |
| ![](./img/hist1_0.png) | ![](./img/hist1_1.png) | ![](./img/hist1_2.png) |



the processed image A

![](./img/img1.png)

The RGB histograms

| R                      | G                      | B                      |
| ---------------------- | ---------------------- | ---------------------- |
| ![](./img/hist2_0.png) | ![](./img/hist2_1.png) | ![](./img/hist2_2.png) |

2.

The processed image B

![](./img/img2.png)

The RGB histograms

| R                      | G                      | B                      |
| ---------------------- | ---------------------- | ---------------------- |
| ![](./img/hist3_0.png) | ![](./img/hist3_1.png) | ![](./img/hist3_2.png) |

3.

The processed image C

![](./img/img3.png)

The RGB histograms

| R                      | G                      | B                      |
| ---------------------- | ---------------------- | ---------------------- |
| ![](./img/hist4_0.png) | ![](./img/hist4_1.png) | ![](./img/hist4_2.png) |

4.

Let A=the image in (1), B= the image in (2), C= the image in (3)

We notice that A is very similar with B, for the RGB components are similar so the overall histogram is similar with each RGB histogram. There are some slight differences which can be seen on the histogram after processed.

Processed in RGB components, the colors of A,B are changed slightly and not so saturated as before, while C keeps the original hue and saturation so result is the best. For instance, the blue on the car on C looks better than A and B.