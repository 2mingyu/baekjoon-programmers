function solution(emergency) {
    sorted_emergency = [...emergency].sort((a, b) => b-a);
    console.log(emergency)
    console.log(sorted_emergency)
    for (let i=0; i<emergency.length; i++) {
        for (let j=0; j<emergency.length; j++) {
            if (emergency[i] == sorted_emergency[j]) {
                emergency[i] = j+1;
                break;
            }
        }
    }
    return emergency
}