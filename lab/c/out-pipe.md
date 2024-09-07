```bash
qnli@OxLiu:~/lab/c$ make
gcc -g -Wall -c foo-pipe.c
gcc -g -Wall -o foo-pipe foo-pipe.o
qnli@OxLiu:~/lab/c$ ./foo-pipe
父进程读取的数据：Child write
父进程读取的数据：Child write
^C
qnli@OxLiu:~/lab/c$
```
