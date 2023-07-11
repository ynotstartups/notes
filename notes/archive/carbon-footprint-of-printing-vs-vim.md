# Carbon Footprint Of Printing Vs Vim

Taken from a conversation from #vim slack channel in Lyst

I am just intrigued to figure out the greenness of printing 1 page v.s. the energy of running note taking program for 1 hour, it wasn't immediate obvious to me which one is greener. :thinking_face:

based on this [quora](https://www.quora.com/What-is-the-carbon-footprint-of-printing-a-single-sheet-of-paper-from-the-printer-itself)

print 4 sheets the printer is producing about 0.00024 pounds of CO2 (about 4 cubic inches of man made greenhouse gas), so

printing 1 page is 0.00006 pounds of CO2 ~ *0.027 gram*

then regarding running note taking program

From [here](https://www.webfx.com/blog/marketing/carbon-footprint-internet/), it mentions *each search* is 0.2 gram :scream:,  so if it is a *web based always online program* such as google keep, then I am guessing running it for an hour will have a *higher* carbon footprint then printing one page.

But we are talking about :vim: here, so what is the carbon footprint of using :vim: for note taking for an hour?

Based on [here](https://www.energuide.be/en/questions-answers/how-much-power-does-a-computer-use-and-how-much-co2-does-that-represent/54/#:~:text=A%20laptop%20uses%20between%2050,falls%20to%20about%20a%20third.) , A laptop that is on for eight hours a day uses between 150 and 300 kWh and emits between 44 and 88 kg of CO2 per year, then CO2 for one hour is 30 gram ( = 88000 / (365 * 8)) .

because vim is a terminal based program and offline so it shouldn't take much energy to run it, say just 1 % then 30\*1% = 0.3 gram , hmm this is 10 times the CO2 compared to printing one page.

Caveat: not counting the CO2 for producing the printers or laptop, or this whole calculate is simply wrong.
