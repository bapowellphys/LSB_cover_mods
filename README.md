LSB_cover_mods includes the code used to perform cover modifications to images prior to LSB embedding in order to secure the resulting stego images against up to third-order structural attacks.  It requires the PIL image library.  

The main file is LSB_cover_mods.py.  It takes as input a singe cover image file and outputs the modified cover image.  It also optionally embeds into this modified cover either 1) a pseudo-random string of maximal length (to simulate an encrypted message, useful for research purposes), or 2) an actual message supplied as an input file.  If either of these options is chosen, the code outputs the stego image.  It also outputs a file containing the trace sets whose pixels were skipped during embedding; this information is needed for message extraction (extraction code is forthcoming).  

Messages are embedded along a pseudo-random path determined by a PRNG; the generator's seed can be considered the secret key that needs to be pre-shared between sender and receiver.

This code is for research and development purposes only.
