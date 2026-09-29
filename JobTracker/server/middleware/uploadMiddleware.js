import multer from 'multer'; import path from 'path'; import fs from 'fs';
const dir=path.resolve('uploads'); fs.mkdirSync(dir,{recursive:true});
const storage=multer.diskStorage({destination:dir,filename:(req,file,cb)=>cb(null,`${Date.now()}-${file.originalname.replace(/[^a-zA-Z0-9._-]/g,'_')}`)});
export const upload=multer({storage,fileFilter:(req,file,cb)=>file.mimetype==='application/pdf'?cb(null,true):cb(new Error('Only PDF resumes are allowed')),limits:{fileSize:5*1024*1024}});
