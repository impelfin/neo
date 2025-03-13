int checkprime(int n) {
    int i;
    for(i=2;i<=n;i++) {
        if(n % i == 0)
            break;
        else
            continue;
    }
    return i;
}
