#include<stdio.h>
int main(){
int ref_str[50], frame[10], pg_no, fr_no, avail, i, j, k, count=0;
printf("\nEnter number of Pages: ");
scanf("%d", &pg_no);
printf("\nEnter number of Frames: ");
scanf("%d", &fr_no);
for(i = 0; i < fr_no; i++)
    frame[i] = -1;
printf("\nEnter Ref String: ");
for(i = 1; i <= pg_no; i++)
    scanf("%d", &ref_str[i]);
j = 0;
printf("Ref string\tpage frames\n");
for(i = 1; i <= pg_no; i++){
    printf("%d\t\t", ref_str[i]);
    avail = 0;
    for(k = 0; k < fr_no; k++)
        if(frame[k] == ref_str[i])
        avail = 1;
        if (avail == 0){
            frame[j] = ref_str[i];
            j = (j + 1) % fr_no;
            count++;
for(k = 0; k < fr_no; k++)
    printf("%d\t", frame[k]);
        }
printf("\n");
}
printf("Total Page Faults: %d", count);
return 0;
}