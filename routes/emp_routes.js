let express=require('express');
let router=express.Router();

router.get("/hr", (req,res)=>{
    res.send("Hr called")
});

router.post("/assign-task",(req,res)=>{
    res.send("hr assigned the work")
});

module.exports=router;