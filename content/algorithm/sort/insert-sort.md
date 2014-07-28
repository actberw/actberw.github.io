void Insertsort(int a[], int n)
{
    int i, j;
    for (i = 1; i < n; i++)
        int temp = a[i];
        for (j = i - 1; j >= 0 && a[j] > temp; j--)
            a[j + 1] = a[j];
        a[j + 1] = temp;
}
