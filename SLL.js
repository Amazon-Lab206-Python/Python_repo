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
    this.Display = function () {   
        var current = this.head;
        var  listy = "";
        while (current) {
            listy += current.value+" => ";
            current = current.next;
        }        
        return listy;
    }

}

function Node(val) { // class definition for Node
    this.value = val; // value is a property and val is the incoming value we want to set this.value to
    this.next = null; // next pointer is null as we don't assume the node have a buddy yet
}

var mySLL = new SLL();
// mySLL.AddFront(56);
// mySLL.AddFront(72);
// mySLL.AddFront(140);
// mySLL.AddFront(12);
// mySLL.AddFront(101);

var node1 = new Node(1);
var node2 = new Node(2);
var node3 = new Node(3);
var node4 = new Node(4);
var node5 = new Node(5);

mySLL.head = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node3;


// console.log(mySLL.max());
// console.log(mySLL.min());

console.log(mySLL);
console.log(mySLL.display());