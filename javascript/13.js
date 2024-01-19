const romanToInt = (s) => {
    const m = {
      I: 1,
      V: 5,
      X: 10,
      L: 50,
      C: 100,
      D: 500,
      M: 1000,
    };
  
    let n = 0;
    let n0, n1;
  
    for (let i = s.length - 1; i >= 0; i--) {
      n0 = m[s[i]];
      n1 = m[s[i - 1]];
  
      if (n1 < n0) {
        n += n0 - n1;
        --i;
      } else {
        n += n0;
      }
    }
  
    return n;
  };