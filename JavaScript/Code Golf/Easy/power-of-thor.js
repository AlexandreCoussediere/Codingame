let[a,b,x,y]=readline().split` `.map(Number);while(1){readline();let m='';if(y!=b)m+=y>b?'N':'S',y+=y>b?-1:1;if(x!=a)m+=x>a?'W':'E',x+=x>a?-1:1;console.log(m)}
