import jwt from 'jsonwebtoken';
export const protect=(req,res,next)=>{try{const h=req.headers.authorization;if(!h?.startsWith('Bearer '))return res.status(401).json({success:false,message:'Authentication required'});const token=h.split(' ')[1];req.user=jwt.verify(token,process.env.JWT_SECRET);next();}catch(e){return res.status(401).json({success:false,message:'Invalid or expired token'});}};
export const adminOnly=(req,res,next)=>req.user?.role==='admin'?next():res.status(403).json({success:false,message:'Admin access required'});
