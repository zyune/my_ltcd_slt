const howsum = (targetSum, number) => {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    if (let num of numbers) {
        const remainder = targetSum - num;
        const remainderResult = howsum(remainder, numbers)
        if (remainderResult!=null) {
            return [...remainderResult, num];
        }
    }
    return null;
        
}
console.log(howsum(7,[2,3]))