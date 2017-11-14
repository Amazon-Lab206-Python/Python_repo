function balance_point(arr){
    var totaltemp = 0;
    var checktemp = 0;
    for( var i = 0; i<arr.length; i++){
        totaltemp += arr[i]
        console.log(totaltemp)
    }
    for( var i = 0; i<arr.length; i++){
        if(checktemp != totaltemp){
            checktemp += arr[i]
            totaltemp -= arr[i]
            console.log(checktemp,',', totaltemp)
        }
        else if(checktemp == totaltemp ){
            console.log(true)
            return true
        }
    }
    console.log(false)
    return false
}

// balance_point([1,2,3,4,10])

function balance_index(arr){
    var temp = 0;
    var totaltemp = 0;
    var checktemp = 0;
    for(var i = 0; i<arr.length; i++){
        totaltemp += arr[i];
        // console.log(totaltemp);
    }
    for(var i = arr.length-1; i > 0; i--){
        totaltemp -= arr[i]
        temp = arr.pop()
        console.log(arr)
        console.log(totaltemp);
        console.log(temp);        
        if(totaltemp != checktemp){
            checktemp += temp
            // console.log(checktemp)
        }
        else if(totaltemp == checktemp){
            return i
            console.log('index:' + i)
        }
        
    }
    console.log(-1);
    return -1;
}

console.log(balance_index([-2,5,7,0,3]))
