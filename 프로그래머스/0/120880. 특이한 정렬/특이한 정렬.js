function solution(array, n) {
    return array.sort((a, b) => {
        const distanceA = Math.abs(a - n);
        const distanceB = Math.abs(b - n);
        
        if (distanceA !== distanceB) {
            return distanceA - distanceB;
        }
        
        return b - a;
    });
}