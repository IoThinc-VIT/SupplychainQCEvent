// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.8.0;

contract Supplychain{

uint256 product_id=0;
uint256 worker_id=0;

struct Product{
    uint256 id;
    string name;
    string price;
    string description;
    string data;
    uint256 timestamp;
}
struct Status{
    string location;
    uint256 timestamp;
    string data;
    uint256 w_id;
    uint256 p_id;
    bool flag;

}

struct Worker{
    string name;
    uint256 id;
    uint256 timestamp;
}

Product[] public products_list;
Product private productInfo;
Status[] public productStatus;
Status private statusInfo;
Worker[] public workers_list;
Worker private workerInfo;

mapping(uint256 => Status[]) public product_Status;
mapping (uint256 => Product) public products;
mapping (uint256 => Worker) public workers;


function setWorker(string memory name) public  payable{
    workerInfo=Worker(name,worker_id,block.timestamp);
    workers[worker_id]=workerInfo;
    workers_list.push(workerInfo);
    worker_id++;

}

function AddProduct(
    string memory name,
    string memory price,
    string memory description,
    string memory data) public payable
{
    productInfo=Product(product_id,name,price,description,data,block.timestamp);
    products[product_id]=(productInfo);
    products_list.push(productInfo);

}

function AddStatus( string memory location,
    
    string  memory data,
    uint256 wid,
    uint256 pid,
    bool flag
) public payable {

    statusInfo= Status(location,block.timestamp,data,wid,pid,flag);
    product_Status[pid].push(statusInfo);
    productStatus.push(statusInfo);
}

function getProductsList() public view returns(Product[] memory)
{
    return products_list;
}

function getWorkerssList() public view returns(Worker[] memory)
{
    return workers_list;
}

function getProductStatus(uint256 id) public view returns(Status[] memory){

    return product_Status[id];
}


}
