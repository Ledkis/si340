function w = hanning(n)
if ~rem(n,2)
   half = n/2;
   w = .5*(1 - cos(2*pi*(1:half)'/(n+1))); 
   w = [w; w(end:-1:1)];
else
   half = (n+1)/2;
   w = .5*(1 - cos(2*pi*(1:half)'/(n+1))); 
   w = [w; w(end-1:-1:1)];
end