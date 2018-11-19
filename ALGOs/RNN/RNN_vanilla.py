'''
Just the forward propagation step implemented
'''

from helper import dot, tanh, random_, add, concat


INPUTS =  [[ 1  , 2    ,1  ],
		   [ 100, 97   ,78 ],
		   [ 100, 1    ,50 ],
		   [ 1  , 100  ,11 ]
		  ]
		  
OUTPUTS=  [[3],
		  ]

sz_input  = len(INPUTS [0] )
sz_hidden = ( len(INPUTS [0] ) + len(OUTPUTS[0] ) ) // 2
sz_output = len(OUTPUTS[0] )

W1     = random_(sz_input  , sz_hidden )
W2     = random_(sz_hidden , sz_hidden )
W3     = random_(sz_hidden , sz_output )
bias   = random_(sz_hidden , 1         )
hidden = random_(sz_hidden , sz_hidden )


for input in INPUTS:
	hidden = tanh(  add(  dot(input,W1),dot(hidden,W2),bias   )  )

output = dot(hidden, W3)
print 'Final Output=',output


# Its better to concat then to add hidden and input since both represents different informations
# one is the overall input till now and the other is just the current input
# adding them (that too without any weightage) gives unreasonably high importance to the current input
# npw, the input and hidden are concatenation though the bias is still added
# Hence, the modification is below -

W1     = random_(sz_input  , sz_hidden )
W2     = random_(sz_input + sz_hidden , sz_hidden )
W3     = random_(sz_hidden , sz_output )
bias   = random_(sz_hidden , 1         )
hidden = random_(sz_input + sz_hidden , sz_hidden )


for input in INPUTS:
	hidden = tanh(  add( concat(dot(input,W1),dot(hidden,W2)) ,bias   )  )

output = dot(hidden, W3)
print 'Final Output=',output


