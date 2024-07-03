function solution(s) {
    let slength= s.length
    let patches = 0

    for(i=0; i<slength; i++){
        if(s[i] === "x"){
             patches++
             i += 2
    }
    }

    return patches
}