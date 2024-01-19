function commonPrefix(s1: string, s2: string): string {
    let r: string = "";
    let i = 0;
    while(i < s1.length && i < s2.length && s1[i] === s2[i]) {
        r += s1[i];
        i++;
    }

    return r;
}

function longestCommonPrefix(strs: string[]): string {
    if(strs.length == 0) return '';
    if(strs.length == 1) return strs[0];
    
    let prefix = strs[0];
    for (let i = 0; i< strs.length; i++) {
        prefix = commonPrefix(prefix, strs[i]);

        if(prefix === '') return prefix;
    }

    return prefix;
};