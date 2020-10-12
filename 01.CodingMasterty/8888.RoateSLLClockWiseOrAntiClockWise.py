# class Node {
#     constructor(val) {
#         this.val = val;
#         this.next = null;
#     }
# }
#
# class SinglyLinkedList {
#     constructor(){
#         this.head = null;
#         this.tail = null;
#         this.length = 0;
#     }
#
#         unshift(val){
#         var newNode = new Node(val);
#         if(!this.head) {
#             this.head = newNode;
#             this.tail = this.head;
#         }
#         newNode.next = this.head;
#         this.head = newNode;
#         this.length++;
#         return this;
#     }
#
#
#
#     push(val) {
#         let newNode = new Node(val);
#         if (!this.head) {
#             this.head = newNode;
#             this.tail = this.head;
#         } else {
#             this.tail.next = newNode;
#             this.tail = newNode;
#         }
#         this.length++;
#         return this;
#     }
#
#
#     rotate(number){
#
#        if (number<0){
#
#            number=this.length-Math.abs(number)
#        }
#
#         number=number%this.length
#
#         for (let i=0;i<number;i++){
#             let value=this.head.val
#             this.head=this.head.next
#             this.push(value)
#             this.length--
#         }
#
#     return this
#     }
#
# }



#
#
# public static void mian(){
#
#     prinln("hellow owrld")
#
#
#
# }
#
#
#












