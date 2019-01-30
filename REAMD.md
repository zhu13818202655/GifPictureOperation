# GIF图片保存方法
>  im.save(out, save_all = True, append_images=[im1, im2......], duration=t)

基本的方法就是这样。out是保存名，append_images是图片list，把想要组合的图片全部放进去就好。

注意这里的im是gif图片的image对象，而list内的图片也是image对象，但是是无要求的，不是gif格式也是可以的。
还有一点，为了美观，在save之前，可以把list里面的图片size，改成和im一样的。（就是改成大小都一样的，不然就会以im的大小为准）
duration=t--->GIF动图的间隔时间
