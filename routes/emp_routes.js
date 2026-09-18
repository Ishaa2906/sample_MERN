let express=require('express');
let router=express.Router();

router.post("/register", (req,res)=>{
    let data=req.body;
    res.send(data.nameco);
});

router.post("/login",(req,res)=>{
    res.send("login page called")
});

router.get("/viewtasks",(req,res)=>{
    res.send("viewtask page called called")
});

router.get("/viewtodos",(req,res)=>{
    res.send("viewtodo's page called")
});

router.put("/updateprofile",(req,res)=>{
    res.send("update profile page called")
});


module.exports=router;