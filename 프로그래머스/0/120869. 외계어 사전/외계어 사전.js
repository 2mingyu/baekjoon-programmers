function solution(spell, dic) {
    const x = spell.sort().join('');
    for (let word of dic) {
        const y = word.split('').sort().join('');
        if (x === y) {
            return 1;
        }
    }
    return 2;
}