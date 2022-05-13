#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <setjmp.h>
#include <stdlib.h>
#include <wait.h>
#include <fcntl.h>

sigjmp_buf o;

void interruptFF(){
    printf("%s","\nInteraptFF\n");
    siglongjmp (o, 1);
}

int main() {
    struct sigaction interrupt;
    interrupt.sa_handler = interruptFF;
    sigemptyset(&interrupt.sa_mask);
    sigprocmask(0, 0, &interrupt.sa_mask);
    interrupt.sa_flags = 0;
    sigaction(SIGINT, &interrupt, 0);

    char b[999];
    char bb[1998][4];

    int dt, dz;

    if((dt=creat("./ab.txt", 1444))==-1) {
        printf("Cannot open file.\n");
        exit (1);
    }
    write(dt, "Generally, any device that can perform numerical calculations, even an adding machine, may be called a computer but nowadays this term is used especially for digital computers. Computers that once weighed 30 tons now may weigh as little as 1.8 kilograms. Microchips and microprocessors have considerably reduced the cost of the electronic components required in a computer. Computers come in many sizes and shapes such as special-purpose, laptop, desktop, minicomputers, supercomputers. Special-purpose computers can perform specific tasks and their operations are limited to the programmes built into their microchips. There computers are the basis for electronic calculators and can be found in thousands of electronic products, including digital watches and automobiles. Basically, these computers do the ordinary arithmetic operations such as addition, subtraction, multiplication and division. General-purpose computers are much more powerful because they can accept new sets of instructions. T", 999);
    close(dt);

    dz = open("./ab.txt", O_RDONLY);

    read(dz, b, 999);
    close(dz);

    int c1[2];
    pipe(c1);
    write(c1[1],b,999);
    close(c1[1]);

    int c3[2];
    pipe(c3);
    sigsetjmp(o,1);
    sleep(1);
    if (fork()==0){
        char b1[999];
        close(c1[1]);
        read(c1[0],b1,999);
        close(c1[0]);
        char b2[4000];
        unsigned i,j;
        for (i=0,j=0; i<3890;){
            if(i<18 && j<10){
                b2[i] = 49 + j;
                b2[i + 1] = b1[j];
                i=i+2;
                j++;
            }
            if(i<288 && i >= 18 ) {
                b2[i] = 49 + ((j + 1) % 100) / 10-1;
                b2[i + 1] = 49 + (j + 1) % 10 - 1;
                b2[i + 2] = b1[j];
                i=i+3;
                j++;
            }
            if(i>=288 && i<3889){
                b2[i] = 49 + (j+1) / 100-1;
                b2[i + 1] = 49 + (((j + 1) % 100) / 10-1);
                b2[i + 2] = 49 + (j + 1)%10-1;
                b2[i + 3] = b1[j];
                i=i+4;
                j++;
            }
        }
        int c2[2];
        pipe(c2);
        write(c2[1],b2,4000);
        close(c2[1]);
            if(fork()==0){
                char b4[4000];
                close(1);
                close(c2[1]);
                read(c2[0],b4,4000);
                close(c2[0]);

                unsigned i2,j2;
                char b3[4885];
                for (i2=0,j2=0;i2<4885;){
                    if (i2<27){
                        b3[i2] = ' ';
                        b3[i2 + 1] = b4[j2];
                        b3[i2 + 2] = b4[j2 + 1];
                        i2=i2+3;
                        j2=j2+2;
                    }
                    if (i2>=27 && i2 <384){
                        b3[i2] = ' ';
                        b3[i2 + 1] = b4[j2];
                        b3[i2 + 2] = b4[j2 + 1];
                        b3[i2 + 3] = b4[j2 + 2];
                        i2=i2+4;
                        j2=j2+3;
                    }
                    if (i2>384 && i2 <4885){
                        b3[i2] = ' ';
                        b3[i2 + 1] = b4[j2];
                        b3[i2 + 2] = b4[j2 + 1];
                        b3[i2 + 3] = b4[j2 + 2];
                        b3[i2 + 4] = b4[j2 + 3];
                        i2=i2+5;
                        j2=j2+4;

                    }
                }
                close(c3[0]);
                write(c3[1],b3,4888);
                _exit(2);
            } else{
                wait(NULL);
                _exit(1);
            }
    } else{
        wait(NULL);
        char n[4888];
        close(c3[1]);
        read(c3[0],n,4887);
        printf("%s\n",n);
        dt = open("./ab.txt", O_WRONLY);
        write(dt,  n, 4887);
        close(dt);
    }
    printf("\nPress Q to exit\n");
    sigsetjmp(o,1);
    while (getchar()!='q'){}
    return 0;
}