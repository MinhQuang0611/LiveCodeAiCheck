#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
int func_a(int difference[], int difference_len){  
    int num = difference[0];  
    for(int i = 0; i < difference_len; i++)  
        if(num < difference[i])     
            num = difference[i]; 
    int ret = 0;    
    for(int i = 0; i < difference_len; i++)  
        if(num == difference[i]){      
            ret = i;      
            break;    
        }    
    return ret;
}  

int func_b(int difference[], int difference_len){  
    int num = difference[0];   
    for(int i = 0; i < difference_len; i++)   
        if(num > difference[i])        
            num = difference[i];  
        int ret = 0;  
        for(int i = 0; i < difference_len; i++)  
            if(num == difference[i]){      
                ret = i;     
                break;     
            }    
        return ret;
}  

int* func_c(int arr1[], int arr1_len, int* arr2, int arr2_len){    
    int* ret = (int*)malloc(sizeof(int)*arr1_len);  
    for(int i = 0; i < arr1_len; i++){   
        int num = arr1[i] - arr2[i]; 
        if(num < 0)         
            num = -num;      
        ret[i] = num;    
    }  
    return ret; 
} 

void solution(int twenty[], int twenty_len, int sixty[], int sixty_len) {  
    int* difference = [[quiz]];   
    int max_diff_idx = [[quiz]];   
    int min_diff_idx = [[quiz]];  
    int* answer = (int*)malloc(sizeof(int)*2); 
    answer[0] = max_diff_idx;
    answer[1] = min_diff_idx; 
    printf("%d,%d",answer[0],answer[1]); 
}