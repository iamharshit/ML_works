'''
Just the forward propagation step implemented
'''

from helper import dot, tanh, random_, add


INPUTS =  [[ 1  , 2    ,1  ],
		   [ 100, 97   ,78 ],
		   [ 100, 1    ,50 ],
		   [ 1  , 100  ,11 ]
		  ]
		  
OUTPUTS=  [[3],
		  ]

sz_input  = len(INPUTS [0] )
sz_output = len(OUTPUTS[0] )

W1     = random_(sz_input  , sz_output )
W2     = random_(sz_output , sz_output )
bias   = random_(sz_output , 1         )
hidden = random_(sz_output , sz_output )


for input in INPUTS:
	output = tanh(  add(  dot(input,W1),dot(hidden,W2),bias   )  )
	hidden = output

print 'Final Output=',output
