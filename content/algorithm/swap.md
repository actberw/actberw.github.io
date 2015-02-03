

void swap_any(void* a, void* b, size_t s){
    void* tmp = malloc(s);
    memcpy(tmp, a, s);
    memcpy(a, b, s);
    memcpy(b, tmp, s);
    free(tmp);
}


#define SWAP(a,b) do { __typeof__(a) temp; temp = a; a = b; b = temp; } while (0)

refer:

- [http://www.linuxcandy.com/2011/11/week-4-introduction-to-generic.html](http://www.linuxcandy.com/2011/11/week-4-introduction-to-generic.html)
- [http://stackoverflow.com/questions/19255069/swap-any-type-of-two-variables-in-c](http://stackoverflow.com/questions/19255069/swap-any-type-of-two-variables-in-c)
