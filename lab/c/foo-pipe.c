#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>

int
main(int argc, char *argv[])
{

    int pipefd[2] = {0};    /* 存放文件描述符 */
    int t = pipe(pipefd);   /* 父进程创建管道, pipe的参数是一个输出型参数 */
    assert(t == 0);

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork 失败");
    } else if (pid > 0) {   /* parent process */
        /* 关闭父进程的写权限 */
        close(pipefd[1]);

        /* 父进程从管道读取数据 */
        char buf[1024] = { 0 };
        while (1) {
            ssize_t ret = read(pipefd[0], buf, sizeof(buf) - 1);

            if (ret > 0) { /* ret存放的是实际读取的字节个数 */
                buf[ret] = '\0';
                printf("父进程读取的数据：%s", buf);
            } else {
                printf("Oops, read nothing!\n");
            }

            sleep(1);
        }
    } else {                /* pid == 0, child preocess */
        /* 关闭子进程的读权限 */
        close(pipefd[0]);

        /* 子进程往管道写入数据 */
        const char *s = "Child write\n";    /* 存放'\n'的作用是刷新缓冲区 */
        while (1) {
            write(pipefd[1], s, strlen(s)); /* 以写权限向管道写入数据 */

            sleep(5);
        }
    }

    return 0;
}
