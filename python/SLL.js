function SLL() { //class definition of SLL
    this.head = null; //head property set to null initially
    //AddFront function that adds a value, therefore node to the front of the SLL
    this.AddFront = function (val) {

        //create the node
        var node = new Node(val);
        // if the head of the SLL is empty, then we can simply set the head to the new node
        if (this.head == null) {
            this.head = node;
        }
        // if the head is occupied, then create a temp to also point to the head so we can manipulate
        // the head to point elsewhere and not lose our previous head node
        // set the head to the new node, then set the new node's .next to the temp (previous head)
        else {
            var temp = this.head;
            this.head = node;
            node.next = temp;
        }
    }
    this.min = function () {
        if(this.head == null){
            return null;
        }
        var current = this.head;
        var min = this.head.value;
        while (current) {
            if (current.value < min) {
                min = current.value;
            }
            current = current.next;
        }
        return min;
    }
    this.max = function(){
        if(this.head == null){
            return null;
        }
        var current = this.head;
        var max = this.head.value;
        while (current) {
            if (current.value > max) {
                max = current.value;
            }
            current = current.next;
        }
        return max;
    }
    this.Display = function(){
        if (this.head == null){
            return null;
        }
        var string = "";
        var current = this.head;
        while(current){
            string = string + current.value + " => ";
            current = current.next;
        }
        return string
    }
    this.prepend = function(val, before){
        if (this.head == null){
            this.head = new Node(val);
            return this
        }
        var current = this.head;
        var temp = 0;
        while(current){
            if(current.next.value == before ){
                // console.log('wow')
                temp = current.next;
                current.next = new Node(val);
                // console.log('temp',temp);
                // console.log(mySLL);
                current = current.next;
                current.next = temp;
                // console.log(mySLL);
            }
        }
        current.next = new Node(val);
        return mySLL;
        // return mySLL;

    }
    this.Contains = function (val) {
        var current = this.head;
        if (this.head == null) {
            return false;
        }else if(current.value == this.head || current.value == this.tail){
            return true;
        }else{
            while (current) {
                if (current.value == val) {
                    return true;
                }
                current = current.next;
            }
            return false;
        }
    }

}

function Node(val) { // class definition for Node
    this.value = val; // value is a property and val is the incoming value we want to set this.value to
    this.next = null; // next pointer is null as we don't assume the node have a buddy yet
}

var mySLL = new SLL();
mySLL.AddFront(0);
mySLL.AddFront(1);
mySLL.AddFront(1);
mySLL.AddFront(2);
mySLL.AddFront(3);
mySLL.AddFront(3);



// console.log(mySLL.max());
// console.log(mySLL.min());
// console.log(mySLL.Display());
console.log(mySLL.prepend(1,5))
console.log(mySLL.Display());