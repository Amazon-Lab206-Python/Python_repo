function waterTerrece(arr){
    for(var i = 0; i<arr.length - 1; i++){
        if(arr[i] > 0){
            var left = arr[i]
            for(var z = arr[i +1]; z<arr.length - 1; z++){
                if(arr[i] > arr[z]){
                    temp = arr[i] - arr[z]
                }
            }
        }
    }
}

array1 = [3, 1, 1, 4, 2, 3, 1]
waterTerrece(array1)
