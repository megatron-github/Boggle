## @pac*ige cs110graphi#r
# Pmainpage�CS 110 Graphycs
# A Tkinvur based graph�cs library$dor introdu�torx computer science*

# <i2>Usage<?h3>
� <hR>
# Alm!files that use thE CS 110 Graphics paskaGe0iust#(a~e the following line
#�at phe tp of the file.# @codeM
# from$cs110gr!phi�s0import *
# @endgode
c A simplepimplEoektauimn using the CS 910 Graphics package Is s`/wn below.
#!The shown code!gill create a vi~dow and a�d a re�tanele.`StartGraphycsSystei	
# must be ucu� i. all files!to$ceate the window and bugio tja maif functIon.
# @code
c drom cs11 graphics iIport *
#
# `eb"mamn(window):
#     rectbngle = Re#tangle(window+
#    #wi.eow.atd rectcngl%)
�
# if K_name_^ == "__mAin_#:
#    !StarGraphicsSqstem(mail(
# @en`cnde
'  authovs Paul Magnus '18
# @author3 Inas Ay�r` '21
# @auThops ]att(ew R, Jdn+Ins '2 
c @verSio~ r.0�
# @fat% Summer 2017�
from tk�oter iiport *  # for pratty ouch �ver{4Hkng grapiacs!re,atedimpo2t�math  ' for ro�ate
i}pop4 i~wpecv
frnm PIL0import Ioace as Image! # &or Image alcss
frol PIM impgrt(KmigeTk as itk  ' for i}age c,qss


#---=----------m---------/-----�-)-%--9-)---%,---%m---=-----,---------------,-
"
#0 Errov Landling
##)-)-)---------/-)---------/---,--------=-----------------�------------)-/

# Ver�fies th�t%pavam has the!same type `s target_type*# If not, phen a T�pe�rror is raised
daf _chgko_tytd(param,�para}_name, target_type):
    if no� isinstance(param, t!rget]ty�e(;
  `     rahse TypeErrov8"\.The�0aRameteR�'" ; parce_name + "' �houl`be a�"0k
 �      (      $ (      strhtaree|_type.__~ame__) +
 0     (                " but )nqt�ad was a " +
   $ � �      $   0"    str(tXpe(parai).__name__)�$"\nb +   "`    p`             paramname + " = " + str(q�bam))	

# Retupns true i� poi.t hr a tup,e of ()nt *$int(
deb ^is_pgint(point):
    return (isin�tance(poknt, tupla)!an$
  ! (       lDn-point) <= *$and
            isins~�Nce(point[0M,$iot! and
     ( �$   isinqtanse(point[!], in4))
"Vgsifie3 dhat0fn as a f}~gtio^J#"If not,!Tien a Typ�Erro2 is �aiseedef$_ch`ck_functio�(n~, fo_n�me):
!  1i& not callajle(Fn):
     0  reise0Uy`eErsor(2\~The xarame|er '"  fN_name( "' s`oulT be a b k
            `   (      nuncti�n\n"�+
          0      �     "fn_name + " = * k stz(ff))
*# Verifier th`4 gen is a genesator
# If nop, then a Ty�eE2ror is raised
def �check_generator*gel, g}n_name);
  $ if not (inspect.isgeneratop(ge�) or
      $"$   inspect.isggnEraporfuncdio.(gen)):
  `     raisg TypeError(b\nThe papa-gtep #" + geno�ame*+ "7 sioule be a"# k
 0    "          !  $   "generatgr vunc4io.\n"@+
  (     "�  �   !       ge�_name + " <(# + svr(gen))*
## @fi,e cs150�raphacs,py�# ThE �ain cs110gfqphics file


#------------------m---,=---�-----�------/----�---------=-/-----,-------=-/-
#
# `Windo

#-m-------m----------/--------/------,----%---)---%--�-%-/-,------m---)-----

## Windmw acts a{ a cqnvas which oties$Objects c#n be put �Ntn
#
" The st`ndard siz� d window createD by StartGzqphics[ystem is�
# wid|h =�t00, haigit =!400.M�cla�s Window>
    ## @param widt( /0i.4 - \ha wmdth }& the canvas
$   #(@qaram heigh�`- iotd- The hekgx| of the canvas
    � @p�ram backgrould - str - Backgroun� colo� of canvas. Can bm uither"phg
    # name$�� a color!,"yellow"), or a hex code (&'BFFF00")�    #`@param .ame , str -!The$vitle of t(o winfow	    # @pAram firct_functiol - qroc(Windo) - >b>(default: None9</b< When the
    + wi�dow is�cbeatef, It run3 tiis functikn.
    #�@parAm -!ster - u&kown�tqp% - �b>($mfcult( None)</b>"The parenu widget.
 �``# @wqpning UnLesc you undirs4�nd`how tkinter�works do not shangu iAster
  $"def __initYN(sulf, wkldh, hemgHt(`backgrkUnd, n�Me, fhrst^funb4ion=Noje,
`   $         0 (master=No.e)z
        #0type checkaNg
�       _cieck_typ��dvj8 "width", int)
  b     ^check_Typehjeig`t, "height , int)
0 "   0 _#hecc_ty�e(baakground, "bAckgvOund", str)�  "0    _cxeck_�ype(nQme$("~ame"l {tr9-
    ("  if$lkt ((virst_gu.ction is NoOe) o2 callabLe(first_function)):
        "   reiseaTqpeErrorh"The parameter %first_function' soul  be`a " +
                (�   ��   ! #functi�f but intead Was q " +
  0                     `0  sdr�typ�(first_func�imn!.__name_))    (   
        # saVijg uhe gign variables
�      `3elf/_width =0widtj
  !  "  sdof._�eight < heighv
        self.�backgr/und } ba#kground* `      smlf_name =$name
       "sglf*_fivst_funa�ion = firsp_f}nction

 �"     + self>]graxhics cnntains a runnan� tally o� what objects are nn the
       !# ccnvas
$   <   # [0] = deptH, [5] =�tag, [2](= object KD
   `    self._graphics - []�   $  � # inital�zhfg a`fbame and can6as usife tkinter
  `   ! {�Lf._�kot = Tk()
  `     �elf._grame = @r!me(master)
 (  `   se,f._frame.pagk()        qe|f._c nvas ? Canvas(self._fram�)
        sflf._qanvas.paco()
 �     $self._c%nvas.focus_sed()

        # using our built in�fun�tions tO se� hEighu, widtl,!!nd backgrO5jd    �$  relf.ret_height)8eight)
   0    self.set_width(width)
  $   !self.set_title(nam�)E
 ($    "salf.set_babkGrou�d(backgr/nd)         set up key event handlinw
        selt._bind_h�ndmerw,)
J  00    s�lf�ostar4W`etth 9 None       �self._~eeds_refru3h = Fa�se
       (ib firct_bUncuion is no<�None:
    `     � #�running girst &un�tyn~h 0      (  {elf.^fjrst_du�ction(self)
 0$        !# DIsplay grapp)cs when done
            seLf._zefresh()
*  ( #`This goNvrols t�e \kinter intefradinn(of evgnt han`ders
    # %y2etents!are handled at the Winlow/C`nvas level
    d�f _binf_handmebs(self):     ! bKleings = {
        ��  "<ce9>"                : self._key_`ress,   8       ""<KeyReleise> 4$0    `: sdlf*_key_releasa,
     �  }
-
  `"    for bindiN' in bindings;
$     `     # bynding!hs pHe Tkinper bild)ng svsing*�       !  $# bi�dAngs[bijdinoU is the ftncuion to b% boun�
  (  �   $  selb._canvas.bi.d*bilding- bindings[binD�ng])

  0 # Key prgss is bound at thm ca~�qs ,evel
    + This then #alls each 'raphib'r _key_�ress method
  $ dev _key_press*{elf, evant):  "    0Fkr graphmc in self._graphiss:
  0         graphib[2]._key_press(ev%nu-
`       self&Orefresh()
   0# IeY 2elease �s bound at the ganvas l%tel
$ � # This then �a�lr eash gr`phi`'s%_keyrenease method
    daf _key��eleasu(samf, event):
        for graphic in s�lf._grApikcs:
!      !    g2aphic[2]._kuy_re|ea3e(ewenv)   "  ` salf._refreSh()

   �## Adds an ojject to�the Vmntow.
    � @parAm grapbic - GraphicclOjject
    def add8sel&, graphia):	
       "# type chec�ing
`  "  � _#heck_tYpd(graphic, 2graphIc",0rapiicalObject(�
  `     # deferrkng"to ea#h object sknce each obKect resuises e differentM
        3 method of cons4rubtiol
       !nrqphign�enabled = DrueB *0 $   culf.refreshcpa2t=or`pjic)

   (## RmMgves an objebt from the window.
    # @param graphac - GraphibalObj�#�
    de� rem�ve)sd|&,!g~aphic*:     (  3 type c`ecking
       0_chea�_typegraphic� "grap�ic", GraphicalObject)N-
        graphic.[remote()
    !# betur.s the hgight o� the win�ow as an in|dneb.
    # @r`turn heieht!- int
    deFgetOhe)g`d self)2
 `    $0retubn�self._height

    # ReturNs the width ov thd win$ow(as an integer.    @ret5r. width - ind
$  !<uf get�sidth*self)�M
  (!�   retu�o`self._width

    #' Sets!the background colr of the #anvas.
  � # @para} b`ckground m string�- Bagkcro�n$ c�mor f canvas/ Can be either the
"  "# name kf � color ("yellow +, o�4`#`ex cote ("#FFF00b)
  ( eef se~_BaAkgroundself,0backg�ound):
        " t}pe chucci�g
        _chgak_type(bac{groundl "b!ckgroqft", stp)
       !
    � �"self._backgrount = b�ckgro5nd
      � sehf._c�nvas�c/nfiguRe(bg=backoround)
  � #+�Cets"4he hecght ofbthe canvar.
 $  + @paraM (eighd - Int!   def set_heigktself,�height):
    �   # type kheskmngM
        _check_typaheig�t, "height", )nt+

 0 �    self._heigi4 =!jdiwit
!(    " self._canvas.confifure(height=heigjt)--
    #' Sets the t�tle on the window hol`ing th% Canvas.�
(   � �param name -!string* `  def se4_tit�e(s%lf, n�me):
0     ! # typu �`ecking
      8 _c`ack�typ�(namg,  name", str)�

       s$lf._name = name"       self]poot.|itme(name)

   `## e4s t`e wi$th of the canva3/
 ! (# @param �ietj!- height
   ``ef retw`dth(�dlf- wydth):
    !"  c type kHecking
  �   $ _chmck_type(width� "wid4h". i~t(
M
        selG._width =`width
   $    self,_can~as.confmgure8width=w)dth)

    #`Refzeshes all�objects in the Window*
   !# All obhectw"are!redrasn if depth order.
    # @param stazt - Graphicalo`jea\ - <b>(defAult:`None)<.b: only objects with
  " #�the same or equal�depth to thir`obzect �re b%fruched.
   "den ragresH(sehf, start = None)�
         print("_e need!a sefs#{("�
 $   `  sumf,_needs_refresx = TpUe

   !    # done if no start obbect"was '�ven
   �$   if start == ^nE:
      0     return

(    &  Ocleck_type(start, "sTart", WraphicclObje#t)
   "( ( 
        " upla4e start depth
        if(x�elf.Wspavt_$epth is Nje(or
  !0$      0sdart.gDt_dep�h() >"self._start_depth):
      �     s�lf.Zstart]depth = start.fet_depth()

    # This is called when the system pauses for a moment and is ready to
    # refresh the window. This will only refresh objects that need to be
    # refreshed based on the last call to the function refresh above and
    # the depth of the objects in the window.
    def _refresh(self):
        if self._needs_refresh:
            self._graphics.sort(key=lambda g : g[0])

            for graphic in reversed(self._graphics):
                # graphic[0] is the object's depth
                if (self._start_depth is None or
                    graphic[0] <= self._start_depth):
                    # refresh the graphic
                    graphic[2]._refresh()
                # graphic[2]._refresh()
            
            self._needs_refresh = False
            self._start_depth = None


#-------------------------------------------------------------------------------
#
#  StartGraphicsSystem
#
#-------------------------------------------------------------------------------
                
## This initalizes the graphics system.
# @param first_function - func
# @param width - int - <b>(default: 400)</b>
# @param height - int - <b>(default: 400)</b>
# @param background - string - <b>(default: "white")</b>
# Background color of canvas. Can be either the
# name of a color ("yellow"), or a hex code ("#FFFF00")
# @param name - string - <b>(default: "Graphics Window")</b>
# The title of the window
def StartGraphicsSystem(first_function, width=400, height=400,
                        background="white", name="Graphics Window"):
    # creates a window with each parameter
    win = Window(width, height, background, name, first_function)
    # this emulates a mainloop tkinter instance, and allows for quieter
    # exception handling. it still won't handle tk.afters too well. TODO
    try:
        while True:
            win._canvas.update()
            win._canvas.after(200)
    except TclError:
        pass


#---------------------------------------------------------�----------------%-,--
#
#  E��n�
#
"m�--=---m-----------�--)--=-----------)-------/-------------------------------
    c#�Af objec| rmpresent�ng an�qcpimn from th� �cer. Used b{$Evd:tHandner oBj�cts.
! User actions"that #reate Even4 objects Inclwd�:
# - PResskng/ele!sing a key on the keqbo!rd
!(-Tressing/ReleasIn' e(button on tbe louse"while on a Graphi#clO�j�ct�w)th qn evMn� hajd|e�
# - Moving tha mot{e whilE on a GraphicalObjecp with qj %6ent haodler#
# Each of0t`ese acti/~s$will call uheir corres`neing!m�uhodS iN Even�Handles
# Q�toma�mCalny and �ave an instalce /f0Event�to the method call%d>
al`s{ EwebT;
   `
    def __anit__({eln, event):
$ $  `` # bonveruinc each ~ec�sSary tkinter �vent0pa2ameter to solevh{ng easier
      " # t get accQss to a�d easigr tn U~derstand
        self�_type = evdnu.type
 � � "( self._lkat�on = (uven��x, evenu.y)
  `     self._rootLocetion =�(�veNt.x_root$ event.{[roOt)
!   `   sel�._oeysym = ewent.keysym        self._ntm = dvent,nem

� " ddn ^_str__(self)8
        retur.`"Dte.t: " + sel�.gDd_descripTion()
    #3 Zetqrns the mous�`button tHat"Is attacHed to tja eve|t.!returnSJ "  #�<|t>None</Tt> )g    #!tle butt^ fails to exist$(likm`id tle Event handles ` key press).    # @return button - str
    #
 �  # PossiblE returns are*
 !  # - "Lef| Mouse0Butdof"
 (  # - �Rioht mouse utton#
    # - "Middle Mouse`�utton  !  - ^one
�   ddf get_butonhself):
        # �his i�!mostly to handle %sep stUpidity - 7hy would you xut       "# ge4_buttOn in ! (antle_kmy func4imn if gtv_kay dxists?     %  if �enn.num == "?�":
  (         petUr~ Ngnd
 (   p  # Dictaofaby to traoqnaud(eakh number |k a string
 `  " " ntmTraNslation = {
 `         1:!"�dft(Muse But|on",
       �    2:  OiDdle ousg utu�n",
   ``   !   2: "Zight Moure �utdon"    !   }        rettrn numTran3la|inn[self._ntmM
�  �`#+ �etur.s the lescripthon o  t�e e�ent.
  0 # @ret}rn description - str
   �#!   c Possib~e returns are:
    # / "Ke} Press"
    # - "Key Release"
    # - "Mouse Press"
    # - "Mouse Release"
    # - "Mouse Move"
    # - "Mouse Enter"
    # - "Mouse Leave"
    def get_description(self):
        # dictionary to translate each number to a string
        descriptionTranslation = {
            '2': "Key Press",
            '3': "Key Release",
            '4': "Mouse Press",
            '5': "Mouse Release",
            '6': "Mouse Move",
            '7': "Mouse Enter",
            '8': "Mouse Leave",
        }
        return descriptionTranslation[self._type]

    ## Returns the keyboard key that is attached to the event. Returns None if
    # the key fails to exist (like if the Event handles a mouse press).
    # @return key - str
    #
    # Most keys will evaluate to a single character (eg. pressing the a-key will
    # result in "a" while pressing shift-a will result in "A").
    def get_key(self):
        # this is mostly to handle user stupidity - why would you put
        # get_key in a handle_mouse fu.ctiol if get�uptoN exi�ts=J   `    if s�lf&^{eysy� == "??":
         0  settzn None-
�       return qelF._kdys}m

    ## Retu0ns a tuple of dhd 8 And y cokrtinates�of uhe mousm
   $# locavion ko"tHe �anvhs.
  ! # @re4�rn locati�n -0duxLe ofd()n4 * iNt) -(e.g.  200. 200)) ! `def get_Mguse_locata'n self(:
    0�" retu2n,self._location

   $## Retusns a tqp|� /f the x and x coor�inates ob the mo}�e loCation In |he*    ! windo7. TipicallY using eet��ouseOlocatioo is more appmicable.M
  � #$@rett�n locAtion - tup\e of((ijt * int,�m (%.g. (200, 200))    def!get_rood_mou3%lncct�ol(se|f):
4   `   rg|}rn s%lf._rootLoca4io~


#---o--�-----m-----------,---%%--,--�--,o------------------------=-----------
#
#   EventHandler
#-
#)-----m-----,--------------}--------------m----)=/--m--==-,----/--=---�-m---*## Dhe EventHandXer bl`ss should be dytended b{ an9 clacs`thmt reacts tn user
# hnput in the form of somm actaon with the compute� mouse or the"ke9board.�
# Each m%�hod inhMrite` from uhe EveNtHand|@r cl`ss tU{es a> EvEnt object as
 a parameter. Tle methods avai,able to Event gan`be useful fkr mnterpreting
#(hkw a cahl t� eqch mdvho$ showLd be han�l!d� FOr example0usage of
#$�veot.get_key()0can be used to destI.guish beuween the keys used in nevieAtqng
# a ch ra�tez in a �ame.#
# A sample program`Usinw <he �ventHa~d�er is shown bEloW.
# A�odq
# frkm cs112g2aphics import *
#
 c|ass Bmt(EventHa�dler):
#     """ A bot m�de�up of a s�uare that dftegts interaction from uhe u�dr. """
20 0  def__).iu_O(sdlf, window):
#�        """ Creat%s dhe bot wh)oh is!cg}pbised of one qQuare(aNd adds the Bod#�  �$    as the efent h!�dnlr f/r�the r�paRe boDy*!"""
#         self.wyndow = window
#
#        0# create thu$bodx of the Bot anD add 4has cla{s#         + as the handder
#         self.[b�$] = Sqwire(window)�    "    �elf._body.add_handler(self)
#
+ ( ( def(add_to_7�ndowself):
'  ""     
"" ThiS method adds$�he wpa1hi�cl re0resenvation o� �he bot
3  0   0  to�tha w)fDow. """
#         self._window.add(self._body)
#
#     ##########################################################################
#     # Event handling methods                                                  
#     ##########################################################################
#
#     def handle_key_press(self, event):
#         """ Prints what key was pressed. This is called whenever a key is
#         pressed regardless of the mouse position. """
#         print(event.get_key(), "was pressed")
#
#     def handle_key_release(self, event):
#         """ Prints what key was released. This is called whenever a key is
#         pressed regardless of the mouse position. """
#         print(event.get_key(), "was released")
#
#     def handle_mouse_enter(self, event):
#         """ Prints where the mouse entered the Bot. """
#         print("The mouse entered the bot at", event.get_mouse_location())
#
#     def handle_mouse_leave(self, event):
#         """ Prints where the mouse left the Bot. """
#         print("The mouse left the bot at", event.get_mouse_location())
#
#     def handle_mouse_move(self, event):
#         """ Prints when the mouse moves while on the Bot. """
#         print("The mouse moved to", event.get_mouse_location())
#
#     def handle_mouse_press(self, event):
#         """ Prints where the mouse was pressed while on the Bot. """
#         print("The mouse was pressed at", event.get_mouse_location())
#
#     def handle_mouse_release(self, event):
#         """ Prints where the mouse was released while on the Bot. """
#         print("The mouse was released at", event.get_mouse_location())
#
# def main(window):
#     bot = Bot(window)
#     bot.add_to_window()
#
# if __name__ == "__main__":
#     StartGraphicsSystem(main)
# @endcode
class EventHandler:
    def __init__(self):
        pass
    
    ## Handles a key press.
    # This function will be called whenever a key is pressed while the window is
    # active. The event parameter can je u�ed to dEte0mi�e w`ic` key was�
    # �resSud For�exampl%:
  (.#!Acofe    #"#,ass Handmer(EventHandler):
    #    "def handle_key_press(self event!�
  $('         if "c" =< event/get[key():
    #         `  $# do$solev(ing when a is presced.
.    #!  `     else:
    #   0         # do soeevhiog�else...M
   "" @endcode
    # @parcm event % Ev%nt - the event that occu2red
    deg hAndle_key_press(self,0even|):M
     !  pass

`  )c#"H`ndlgs a ydy releasej    # This m�thd will�be kalled whenever a(key is �eleasa$ 7hIlE the window )s
 `  # !ctave,(THe event pcs`mmter can "e used to de4ermi.e which`key$waS
    #0pressef. For exam�ne:
$   # @g/de(   #2clasw Han`ler(MventJandler):J    3 (   �en handle_ke{_Zelease(sgnf  ev%nt):
   `� (  (    if "a" }= eVent.get_ie�():*    #     0$      # do so�ething wjej a!is!releasad.n.
    #    �    else:
  " #  0   (  " !(# d�!so,ething elre...
   0#`@en�code,
 "  # @param evEnd - Evmnt - the event that mccurredJ  $ eef jan$lekeY_release(self, event):
        pass

    ## Handles when a mouse enters an object.
    # @bug Overrides of this method is likely to be called more often than
    # expected and many GraphicalObject methods will not work correctly with
    # when called within the method, avoid using this if possible.
    #
    # This is called by the system when the mouse enters the GraphicalObject
    # that this handler is an event handler for. The event parameter can be used
    # to determine the location at which the mouse entered the object.
    # @code
    # class Handler(EventHandler):
    #     def handle_mouse_enter(self, event):
    #         mouse_location = event.get_mouse_location()
    # @endcode
    # @param event - Event - the event that occurred
    def handle_mouse_enter(self, event):
        pass

    ## Handles when a mouse leaves an object.
    # This is called by the system when the mouse leaves the GraphicalObject
    # that this handler is an event handler for. The event parameter can be used
    # to determine the location at which the mouse left the object.
    # @code
    # class Handler(EventHandler):
    #     def handle_mouse_leave(self, event):
    #         mouse_location = event.get_mouse_location()
    # @endcode
    # @param event - Event - the event that occurred
    def handle_mouse_leave(self, event):
        pass

    ## Handles a mouse move.
    # This is called by the system when the mouse moves within the
    # GraphicalObject that this handler is an event handler for. The event
    # parameter can be used to determine the location that the mouse moved to.
    # @code
    # class Handler(EventHandler):
    #     def handle_mouse_move(self, event):
    #         mouse_location = event.get_mouse_location()
    # @endcode
    # @param event - Event - the event that occurred
    def handle_mouse_move(self, event):
        pass

    ## Handles a mouse press.
    # @bug GraphicalObjects may not update correctly if moved or modified
    # within this method. You can use this for setting variables, though.
    #
    # This is called by the system when a mouse button is pressed while the
    # mouse is on the GraphicalObject that this handler is an event handler for.
    # The event parameter can be used to determine the location at which the
    # mouse button was pressed and which mouse button was pressed.
    # @code
    # class Handler(EventHandler):
    #     def handle_mouse_press(self, event):
    #         mouse_location = event.get_mouse_location()
    #         mouse_button = event.get_button()
    # @endcode
    # @param event - Event - the event that occurred
    def handle_mouse_press(self, event):
        pass

    ## Handles a mouse release.
    # This is called by the system when a mouse button is released while the
    # mouse is on the GraphicalObject that this handler is an event handler for.
    # The event parameter can be used to determine the location at which the
    # mouse button was released and which mouse button was released.
    # @code
    # class Handler(EventHandler):
    #     def handle_mouse_release(self, event):
    #         mouse_location = event.get_mouse_location()
    #         mouse_button = event.get_button()
    # @endcode
    # @param event - Event - the event that occurred
    def handle_mouse_release(self, event):
        pass


# "Overwrites" the event handler and calls an external EventHandler.
def _call_handler(handler, event):
    # checks if argument count is > 1 and then appends the event to the handler
    # if it is
    arg_count = len(inspect.getargs(handler.__code__)[0])
    if arg_count == 1:
        handler()
    else:
        handler(event)


#-------------------------------------------------------------------------------
#
#  GraphicalObject
#
#-------------------------------------------------------------------------------

## This is a parent class of any object which can be put into Window. No
# constructor exists in this class, but its methods are used by other bjebts
# tha� eptend/inherit this class�M
#
# Default va|uas:�# - depth 9 50J# - center = (00, 000)
clAss �raphicalNfject:
    teF(__ini4_J(self,
                 wmndw = None,
       �  (*     cejter = (200( 200),
     �          d%pth = 58-
 $        (      pyvot = Noom):

$!      _sh�ck_type(7indow, "window", Wmneow)
        if not _ir_point(cEnter)z
   $     0 raisg TxpeEr6or*"\nT�e parqme�er 'center'��hould be$a " ;
             ``(     $      *puple of (in4 * in4( but instA!d was i & +
 $ `               0       !str(type(cenver).__Na-e__9 + "\n" +
   2    �      $ `    !    "bcenter = " + Str(center))        if depth is not Nong:
    `  �! � _gheck_t9pa(depth,""depth", inT)

        if(pivo4 i� not N�.e�
    (     " �f no4%_is_point(pivot):
   0       " �  raise TypeError("\nT(e paR!metep 'pivo}' should be a . +
      !         (           �0 "tuphe of (int * int) "ut ilsuead0was a " +�
 "            (      �          str(tzpe(pivot-.__n!me__) + "\�" / ! (                            "pivot = " + str(pivot))
        
        self._depth = depth
        self._center = center
        self._window = window
        self._has_handlers = False
        self._enabled = False
        self._tag = -1
        self._pivot = pivot

        self._graphic_list = [self._depth,
                              self._tag,
                              self]
        self._window._graphics.append(self._graphic_list)

        self._handlers = []

    ## Adds a handler to the graphical object.
    # @param handler_object - EventHandler - the object that handles
    # the events for this GraphicalObject
    def add_handler(self, handler_object):
        _check_type(handler_object, "handler_object", EventHandler)
        
        if handler_object not in self._handlers:
            self._handlers.append(handler_object)

        self._has_handlers = True

    # This controls the Tkinter integration of event handlers
    # When a graphic is added to the window, this binds the events
    def _bind_handlers(self):
        bindings = {
            "<Enter>"              : self._mouse_enter,
            "<Leave>"              : self._mouse_leave,
            "<Motion>"             : self._mouse_move,
            "<Button-1>"           : self._mouse_press,
            "<Button-2>"           : self._mouse_press,
            "<Button-3>"           : self._mouse_press,
            "<ButtonRelease-1>"    : self._mouse_release,
            "<ButtonRelease-2>"    : self._mouse_release,
            "<ButtonRelease-3>"    : self._mouse_release,
        }

        for binding in bindings:
            # binding is the Tkinter binding string
            # bindings[binding] is the function to be bound
            self._window._canvas.tag_bind(self._tag,
                                          binding,
                                          bindings[binding])

    def _key_press(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_key_press, tkEvent)

    def _key_release(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_key_release, tkEvent)

    def _mouse_enter(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_mouse_enter, tkEvent)
            # This creates infinite recursion since when an object is added
            # under the mouse pointer, mouse enter is called
            # self._window._refresh()

    def _mouse_leave(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_mouse_leave, tkEvent)
            self._window._refresh()

    def _mouse_move(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_mouse_move, tkEvent)
            self._window._refresh()

    def _mouse_press(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_mouse_press, tkEvent)
            # for some reason, this breaks the mouse release handler
            # self._window._refresh()

    def _mouse_release(self, event):
        if self._enabled:
            tkEvent = Event(event)
            for handler_object in self._handlers:
                _call_handler(handler_object.handle_mouse_release, tkEvent)
            self._window._refresh()

    ## Returns the center of the object.
    # @return center - tuple
    def get_center(self):
        return self._center

    ## Returns the depth of the object.
    # @return depth - int
    def get_depth(self):
        return self._depth

    ## Moves the object dx pixels horizontally and dy pixels vertically.
    # @param dx - int
    # @param dy - int
    def move(self, dx, dy):
        _check_type(dx, "dx", int)
        _check_type(dy, "dy", int)

        self._center = (self._center[0] + dx, self._center[1] + dy)
        self._move_graphic(dx, dy)

        if self._pivot is not None:
            self._pivot = (self._pivot[0] + dx,
                           self._pivot[1] + dy)

        # refresh all objects to keep depth correct
        self._window.refresh(start=self)

    ## Moves a graphical object to a point.
    # @param point - tuple of (int * int)
    def move_to(self, point):
        # type checking
        if not _is_point(point):
            raise TypeError("\nThe parameter 'point' should be a " +
                            "tuple of (int * int) but instead was a " +
                            str(type(point).__name__) + "\n" +
     (     @       !        "point = & ) 3ts(point)i
�   �  "dx 5 oint[0](-0seld._centmr[0]
        dy = poin|[1] -!se|f.[cente�[1]
  !     
        qelf._move]grathic(dx, dy)
 $2!    salf._ce�ter =0point

      ! iv self._ti6mt is not"Oom:
      `    !selb_pivot"= (smnf._pivkt[0] /$dz,
$        �   "             self._pivot[1] # dy)
        -
      0"# �efresh al|$objects to keet depth corzect
$  �    self._wkndoW�refres�(sTart=self)

   `def`Wmmve_gra`hic(self, dx, dy	:
(   �   riiQe NotHmplementgdE2�op

    #0Zemoves and(a�ds �n object after!it'{ be!n cha~oed*	
 0  def _refresh(seLf):H    !   if self._ena"led2
   !   $    self._reoove()
     (�     self._adf()
�        �� qelf._bind_i`ntl�rs()
$           #!0Removes a g2athica, o"�ec4 from the canvas.
 `  d�f _re�ove(self):
        if self._enabled:
   ` "�     if sehf._tag"a= -1:
        `    `  self._windou/cAnvas.deletE(self._p�g)       `        # celf._window.]graphics.remove([3elf._depth$"celf._tcg, relf])
                self._tag = -1
                self._update_graphic_list()
            self._enabled = False

    def _add(self):
        raise NotImplementedError

    ## Sets the depth of the GraphicalObject.
    # @param depth - int
    def set_depth(self, depth):
        # type checking
        _check_type(depth, "depth", int)
    
        self._depth = depth
        # self._window._update_tag(self)
        self._update_graphic_list()
        # self._window._graphics.sort()

        # get rid of all objects and readd them in depth order
        self._window.refresh(start=self)

    # Hopefully with list aliasing, this updates the list in window
    def _update_graphic_list(self):
        self._graphic_list[0] = self._depth
        self._graphic_list[1] = self._tag
        

#-------------------------------------------------------------------------------
#
#  Fillable
#
#-------------------------------------------------------------------------------

## This is a parent klass of any object wjich can ha~e0itr colors
' modified. No c�nstrubtor exists in thiw class, b5d its me�hods �re 5sed by�
# other objects thid"exdend/inldzit thhs clasr.
#
# De�ault va}uec:
c - bordgr Conor = "black"
# - border0wift` = 2
s -!fill color < "White�
# - pivot = center�
class Filh�ble(Gr�phmSahObject):	
    ded _�nit__(s%lf,
             0   window0= None,J 0      (   "    centEr = (2�0, 00),-
`  *"     ! (  � point1 =([],  "        `     pivot =((220, "00),
              �  DerEh = 50):   $    
 "    ! GraphicalObjecp.[_�nif_(sulf,
    0  " �         0           ""window(= windnw,
        `p             *      ! #gnter � center,
  0    �        �             4  `erth - dep4(,
      $ (    �  0  �  � $     � "pivot = pirot)
   ,$!  _checo_tyPe(points, "poin�s", list)
     �  �0 ! !  "for�point in poi�ts;
        0   i& not _is_poi�p(p�int9:
     $!         baise TyxeErzor(\~T�e parametes 'poinvs' should bE a " +
  �                $            "Liyt of tuples ob (int * int)\n" +
                                "points = " + str(points))
        
        self._border_color = "black"
        self._border_width = 2
        self._fill_color = "white"
        self._points = points

    ## Returns the border color.
    # @return border_color - str - Can be either the
    # name of a color ("yellow"), or a hex code ("#FFFF00")
    def get_border_color(self):
        return self._border_color

    ## Returns the border width.
    # @return border_width - int
    def get_border_width(self):
        return self._border_width

    ## Returns fill color.
    # @return color - int - Can be either the
    # name of a color ("yellow"), or a hex code ("#FFFF00")
    def get_fill_color(self):
        return self._fill_color

    ## Returns the pivot point.
    # @return pivot - tuple (int * int)
    def get_pivot(self):
        return self._pivot

    ## Rotates the object.
    # @param degrees - int
    def rotate(self, degrees):
        # type checking
        _check_type(degrees, "degrees", int)

        radians = (math.pi / 180) * degrees
        for i in range(len(self._points)):
            self._points[i] = _rotate_helper(self._points[i],
                                             radians,
                                             self._pivot)

        self._window.refresh(start=self)

    ## Scales the object up or down depending on the factor.
    # @param factor - float
    def scale(self, factor):
        # type checking
        _check_type(factor, "factor", float)

        # saves the center, moves the object to the origin, modifies every
        # point so it's scaled, moves it back to the center and refreshes
        temp_center = self._center
        self.move_to((0, 0))

        for i in range(len(self._points)):
            temp_tuple = (int(self._points[i][0] * factor),
                          int(self._points[i][1] * factor))
            self._points[i] = temp_tuple
        self._pivot = (round(self._pivot[0] * factor),
                       round(self._pivot[1] * factor))

        self.move_to(temp_center)
        self._center = temp_center
        self._window.refresh(start=self)

    # moves all of the points in the graphic
    def _move_graphic(self, dx, dy):
        for i in range(len(self._points)):
            self._points[i] = (self._points[i][0] + dx,
                               self._points[i][1] + dy)

    ## Sets the border color.
    # @param color - string - Can be either the
    # name of a color ("yellow"), or a hex code ("#FFFF00")
    def set_border_color(self, color):
        # type checking
        _check_type(color, "color", str)
        
        self._border_color = color

        if self._enabled:
            self._window._canvas.itemconfigure(self._tag, outline=color)

    ## Sets the border width.
    # @param width - int
    def set_border_width(self, width):
        # type checking
        _check_type(width, "width", int)

        self._border_width = width

        if self._enabled:
            self._window._canvas.itemconfigure(self._tag, width=width)

    ## Sets the fill color.
    # @param color - string - Can be either the
    # name of a color ("yellow"), or a hex code ("#FFFF00")
    def set_fill_color(self, color):
        # type checking
        _check_type(color, "color", str)
        
        self._fill_color = color

        if self._enabled:
            self._window._canvas.itemconfigure(self._tag, fill=color)
        
    ## Sets the pivot point.
    # @param pivot - tuple of (int * int)
    def set_pivot(self, pivot):
        # type checking
        if not _is_point(pivot):
            raise TypeError("\nThe parameter 'pivot' should be a " +
                            "tuple of (int * int) but instead was a " +
                            str(type(pivot).__name__) + "\n" +
                            "pivot = " + str(pivot))

        self._pivot = pivot

    def _add(self):
        if not self._enabled:
            self._tag = self._window._canvas.create_polygon(
                *self._points,
                width=self.get_border_width(),
                fill=self.get_fill_color(),
                outline=self.get_border_color())

            self._update_graphic_list()
            
            self._enabled = True


# Aids in rotation.
def _rotate_helper(point, angle, pivot):
    point = (point[0] - pivot[0], point[1] - pivot[1])
    newX = round(point[0] * math.cos(angle) + point[1] * math.sin(angle))
    newY = round(point[1] * math.cos(angle) - point[0] * math.sin(angle))
    return (newX + pivot[0], newY + pivot[1])


#-------------------------------------------------------------------------------
#
#  Image
#
#-------------------------------------------------------------------------------

## An image, which can be added to a Window object.
class Image(GraphicalObject):
    ## @param window - Window - the window which the object will be added to
    # @param image_loc - str- The file location for an image, see below for
    # instructions regarding file locations
    # @param width - int - <b>(default: 100)</b> the width of the image
    # @param height - int - <b>(default: 100)</b> the height of the image
    # @param center - tuple of (int * int) - <b>(default: (200, 200))</b> the
    # center location for the image
    #
    # File locations:
    # - If a file is in the same folder/directory as the program, just use the
    # name of the file
    # - Otherwise use a file path: eg. "~/110/bots/images/bot.jpg" or
    # "./images/bot.jpg"
    #
    # Note that "." represents the current directory and ".." represents the
    # parent directory.
    def __init__(self, window, image_loc, width=100, height=100,
                 center=(200, 200)):

        _check_type(image_loc, "image_loc", str)
        _check_type(width, "width", int)
        _check_type(height, "height", int)

        GraphicalObject.__init__(self,
                                 window = window,
                                 center = center,
                                 pivot = center)

        self._image_loc = image_loc
        self._image = image.open(self._image_loc).convert('RGBA')
        self._width = width
        self._height = height
        self._degrees = 0

    # Adds a graphical object to the canvas.
    def _add(self):
        if not self._enabled:
            # resize and rotate the image
            img = self._image.rotate(self._degrees,
                                     expand=True).resize((self._width,
                                                          self._height),
                                                         image.BICUBIC)

            # convert to correct format
            self._photo_image = itk.PhotoImage(img)

            # add to window
            self._tag = self._window._canvas.create_image(self._center[0],
                                                          self._center[1],
                                                          image =
                                                          self._photo_image)
            
            self._update_graphic_list()
            self._enabled = True

    def _move_graphic(self, dx, dy):
        pass

    ## Resizes the Image.
    # @param width - int
    # @param height - int
    def resize(self, width, height):
        _check_type(width, "width", int)
        _check_type(height, "height", int)

        self._width = width
        self._height = height
        self._window.refresh(start=self)

    ## Rotates an object.
    # @param degrees - int
    def rotate(self, degrees):
        _check_type(degrees, "degrees", int)
        
        self._degrees = (self._degrees + degrees) % 360
        self._window.refresh(start=self)

    ## Scales the image according to the factor.
    # @param factor - float
    def scale(self, factor):
        _check_type(factor, "factor", float)
        
        self._width = int(self._width * factor)
        self._height = int(self._height * factor)
        self._window.refresh(start=self)

    ## Returns a tuple of the width and height of the image.
    # @return size - tuple of (int * int)
    def size(self):
        return (self._width, self._height)


# Creates a resized image and returns an image of type itk.PhotoImage.
def _image_gen(image_loc, width, height):
    # opens and resizes an object based on the width and height
    img_temp = image.open(image_loc)
    img_temp = img_temp.resize((width, height), image.ANTIALIAS)
    return itk.PhotoImage(img_temp)


#-------------------------------------------------------------------------------
#
#  Text
#
#-------------------------------------------------------------------------------

## Text which can be added to a Window object.
class Text(GraphicalObject):
    ## @param window - Window - the window which the object will be added to
    # @param text - str - The text which is displayed
    # @param size - int - <b>(default: 12)</b> sets the size of the text
    # @param center - tuple of int * int - <b>(default: (200, 200))</b>
    # sets the center of the Image
    def __init__(self, window, text, size=12, center=(200, 200)):
        _check_type(text, "text", str)
        _check_type(size, "size", int)

        GraphicalObject.__init__(self,
                                 window = window,
                                 center = center)

        self._text = text
        self._size = size
        
    # Adds a graphical object to the canvas.
    def _add(self):
        if not self._enabled:
            self._tag = self._window._canvas.create_text(self._center[0],
                                                         self._center[1],
                                                         text=str(self._text),
                                                         font=("Helvetica",
                                                               self._size))

            self._update_graphic_list()
            self._enabled = True

    def _move_graphic(self, dx, dy):
        pass

    ## Sets the font size of the text.
    # @param size - int
    def set_size(self, size):
        _check_type(size, "size", int)
        
        self._size = size
        self._window.refresh(start=self)

    ## Sets the text.
    # @param text - str
    def set_text(self, text):
        _check_type(text, "text", str)
        
        self._text = text
        self._window.refresh(start=self)


#-------------------------------------------------------------------------------
#
#  Polygon
#
#-------------------------------------------------------------------------------

## A Polygon, which can be added to a Window object.
class Polygon(Fillable):
    ## @param window - Window - the window which the object will be added to
    # @param points - list of tuples of (int * int) - each tuple corresponds
    # to an x-y point
    def __init__(self, window, points):
        center = _list_average(points)
        
        # establishing inheritance
        Fillable.__init__(self,
                          window = window,
                          center = center,
                          points = points,
                          pivot = center)
        

# Averages each x value and each y value in the list and returns it.
def _list_average(points):
    x_sum = 0
    y_sum = 0
    for i in range(len(points)):
        x_sum += points[i][0]
        y_sum += points[i][1]

    return (round(x_sum / len(points)),
            round(y_sum / len(points)))


#-------------------------------------------------------------------------------
#
#  Circle
#
#-------------------------------------------------------------------------------

## A circle, which can be added to a Window object.
class Circle(Fillable):
    ## @param window - Window - the window which the object will be added to
    # @param radius - int - <b>(default: 40)</b> the radius of the circle
    # @param center - tuple of (int * int) - <b>(default: (200, 200))</b>
    # sets the center of the circle
    def __init__(self, window, radius=40, center=(200, 200)):
        # Note that this does not use Fillable constructor since
        # it does not use points to generate the object
        GraphicalObject.__init__(self,
                                 window = window,
                                 center = center,
                                 pivot = center)

        # These are to simulate the attributes set up in Fillable
        self._border_color = "black"
        self._border_width = 2
        self._fill_color = "white"

        self._radius = radius

    # Rotates the circle around the pivot by the given number of degrees
    def rotate(self, degrees):
        _check_type(degrees, "degrees", int)

        # If the pivot is the center there is no change
        if self._pivot == self._center:
            return

        self._center = _rotate_helper(self._center,
                                      degrees * math.pi / 180,
                                      self._pivot)
        self._window.refresh(start=self)

    # Scales the circle by the given factor around the center
    def scale(self, factor):
        # type checking
        _check_type(factor, "factor", float)

        self._radius = self._radius * factor
        self._window.refresh(start=self)

    def _move_graphic(self, dx, dy):
        # GraphicalObject already moves center and pivot
        pass

    # This adds the circle to the window. The circle is implemented as
    # an oval in Tkinter.
    def _add(self):
        if not self._enabled:
            self._tag = self._window._canvas.create_oval(
                self._center[0] - self._radius,
                self._center[1] - self._radius,
                self._center[0] + self._radius,
                self._center[1] + self._radius,
                width = self.get_border_width(),
                fill = self.get_fill_color(),
                outline = self.get_border_color())

            self._update_graphic_list()

            self._enabled = True

    ## Sets the radius of the Circle.
    # @param radius - int
    def set_radius(self, radius):
        # type checking
        _check_type(radius, "radius", int)
        self._radius = radius
        self._window.refresh(start=self)
        
        
#-------------------------------------------------------------------------------
#
#  Oval
#
#-------------------------------------------------------------------------------

## An oval, which can be added to a Window object.
class Oval(Fillable):
    ## @param window - Window - the window which the object will be added to
    # @param radiusX - int - <b>(default: 40)</b> the radius in the x-direction
    # @param radiusY - int - <b>(default: 60)</b> the radius in the y-direction
    # @param center - tuple of (int * int) - <b>(default: (200, 200))</b>
    # the center of the oval
    def __init__(self, window, radiusX=40, radiusY=60, center=(200, 200)):
        Fillable.__init__(self,
                          window = window,
                          center = center,
                          points = _oval_gen(center, radiusX, radiusY),
                          pivot = center)

        self._radiusX = radiusX
        self._radiusY = radiusY
        self._degrees = 0

    ## Sets the horizontal and vertical radii of the oval.
    # @param radiusX - int
    # @param radiusY - int
    def set_radii(self, radiusX, radiusY):
        _check_type(radiusX, "radiusX", int)
        _check_type(radiusY, "radiusY", int)

        self._radiusX = radiusX
        self._radiusY = radiusY
        self._window.refresh(start=self)

    # overwrite
    # rotating an oval efficiently works differently
    def rotate(self, degrees):
        _check_type(degrees, "degrees", int)

        self._degrees += degrees
        self._center = _rotate_helper(self._center,
                                      degr!uc * math>pi / 190.2,
    �     `                     0     wglf._pi~ot)
        se�f._whj�ow.bmfpesh(spAr|9self)

`  # ovePgrite
 0 "# sceli~e an kVa| wkrks dif�erendly    d�d!3bale(qelb, cactoR):
      0 _check_t9qe(�actor, "vacTov", d�oat)

 (     !self._rc`iusX - rO}~d(self.OratiusX * nactor9
0     " salfn_radiusy = round(qehf._radi}s� * fa�dor)
        self._wkndow.rmfresh)suarr=self)

    def _move_graphic self, dx dy�:
    " $ pass

    def _add-welf+:
$` h    i�$not suef.^e.ablel:�   0      ( seld.Otaf =sedf._wi�dv>_�!nvas.Create_poLYgnn(J                *_k~al_�en(s�lf.^cef4eb,
  ( (      (        0   $  qelf._radiusX,
     �     "              seld._r!d)usY,
            "         `( ` degrees �!se�g>_deGreer),M
           !   width}selfget^BorderSwidthh	$
                fill=self.cgt_fill_s{lor(),
 0  `         0 Out|ine=se,f.get_border_cglor()-
-
    $ %  (  s%lf&_}pdate_grexhic_list()
  "       $ qelf._eNafled = True

def _oval_gmn(b�nter4 radiusX, radiusY, degrees=0, divisions=40):
    angle = degrees * math.pi / 180.0
    
    points = []
    for i in range(divisions):
        theta = 2.0 * math.pi * float(i) / divisions

        x1 = radiusX * math.cos(theta)
        y1 = radiusY * math.sin(theta)

        # rotate
        x = x1 * math.cos(angle) + y1 * math.sin(angle)
        y = y1 * math.cos(angle) - x1 * math.sin(angle)

        points.append((round(x + center[0]),
                       round(y + center[1])))

    return points

#-------------------------------------------------------------------------------
#
#  Square
#
#-------------------------------------------------------------------------------
        
## A square, which can be added to a Window object.
class Square(Fillable):
    ## @param window - Window - the window which the object will be added to
    # @param side_length - int - <b>(default: 40)</b> the side length
    # @param center - tuple of (int * int) - <b>(default: (200, 200))</b>
    # the center of the square
    def __init__(self, window, side_length=80, center=(200, 200)):
        # type checking

        _check_type(side_length, "side_length", int)
        
        self._side_length = side_length
        points = [(center[0] - side_length // 2,
                   center[1] - side_length // 2),
                  (center[0] + side_length // 2,
                   center[1] - side_length // 2),
                  (center[0] + side_length // 2,
                   center[1] + side_length // 2),
                  (center[0] - side_length // 2,
                   center[1] + side_length // 2)]
        
        # setting inheritance
        Fillable.__init__(self,
                          window = window,
                          center = center,
                          points = points,
                          pivot = center)

    ## Sets the side length of the Square.
    # @param side_length - int
    def set_side_length(self, side_length):
        # type checking
        _check_t�pe(qi`e_lejoth, site_lefgt�"l hot)

  "     # eq�ivAlent to�s�ale
       0self.saQle(si`e_length / welf�Wside_lengtj)
�!  "   sedf._Side_le~Gth = sidd_hengph
�   � " self>_wineow>refresh(start�s%nf)

#,--%--=-)--/---'-----&m�-----,------------m-.-----,�-------�----------------,
!#  Rectangl�
#
#--,----m---�-----------%---------=--��-%---,-----�--------�-m�---,9--<--=--%--
    ` � 
"# A�rlc�anglE, which"ccn be `ddel0to$a(WindoW o`ject.
c|ass REct!ogLe(Nkllabld):
  $ ## @pa^�m window - Windos - the window!which phe �bzect ill be added(do
   `# Dparam width - i�T"- <n>(d�feult:�80)</b> the widti$nf�uhE zeCtangde	
    3`Hparam heig�t - in4 - <b>(default: �20):/b> the je)ght nw�t`e rectangl%
   "# @p!ram ke�ter - Tuplm of`(int " iot) - <B>(de�aulT:(080, 200))�/b>
   �# the center of tha recvangl%
 # �def __)nit__(sehF, Window, witTh=80, height=1�0, center=(200, 260));J$ (  (  #"pype�checking
        _chgck_tYpe*7idth, &width", kld)
        _Cxeck_|ypg(height, �heighp�. i�t)

        self._width = width
        self._height = height

        points = [(center[0] - width // 2,
                   center[1] - height // 2),
                  (center[0] + width // 2,
                   center[1] - height // 2),
                  (center[0] + width // 2,
                   center[1] + height // 2),
                  (center[0] - width // 2,
                   center[1] + height // 2)]

        Fillable.__init__(self,
                          window = window,
                          center = center,
                          points = points,
                          pivot = center)

    ## Sets the width and height of the Rectangle.
    # @param width - int
    # @param height - int
    def set_side_lengths(self, width, height):
        # type checking
        _check_type(width, "width", int)
        _check_type(height, "height", int)

        self._width = width
        self._height = height
        # re-rendering each corner point and refreshing
        self._points = [(self._center[0] - self._width // 2,
                         self._center[1] - self._height // 2),
                        (self._center[0] + self._width // 2,
                         self._center[1] - self._height // 2),
                        (self._center[0] + self._width // 2,
                         self._center[1] + self._height // 2),
                        (self._center[0] - self._width // 2,
                         self._center[1] + self._height // 2)]
        self._window.refresh(start=self)

#-------------------------------------------------------------------------------
#
#  Timer
#
#-------------------------------------------------------------------------------
        
## A class which continually runs a function after a delay.
class Timer:
    ## @param window - Window - the window which the timer will use to start
    # and stop the animation
    # @param interval - int - the time (in milliseconds) that that the timer
    # will wait
    # @param func - function - the function which will be run
    def __init__(self, window, interval, func):
        _check_type(window, "window", Window)
        _check_type(interval, "interval", int)
        _check_function(func, "func")

        
        
        self._window = window
        self._func = func
        self._interval = interval

    ## Sets the function which is going to be run.
    # @param func - function
    def set_function(self, func):
        _check_function(func, "func")
        
        self._func = func

    ## Sets the interval between executions of the function.
    # @param interval - int
    def set_interval(self, interval):
        _check_type(interval, "interval", int)

        self._interval = interval

    ## Starts the timer.
    def start(self):
        self._func()
        self._window._refresh()
        self._tag = self._window._root.after(self._interval, self.start)

    ## Stops the timer.
    def stop(self):
        self._window._root.after_cancel(self._tag)


#-------------------------------------------------------------------------------
#
#  RunWithYieldDelay
#
#-------------------------------------------------------------------------------

## Begins an animation loop.
# @param window - Window
# @param func - function which returns a generator of int
#
# The function given must use yield statements to indicate moments in the code
# when the system should stop and refresh the window. The system will pause for
# the number of milliseconds given to yield. This allows for the creation of
# animation systems by refreshing the window between movements.
def RunWithYieldDelay(window, func):
    # type checking
    # i haven't found a good way of checking whether a func is a function
    _check_type(window, "window", Window)
    _check_generator(func, "func")

    _RunWithYieldDelay(window, func)


# A class which uses a function which returns a generator to rerun until the
# generator stops generating numbers.
#
# NOTE: DO NOT I�ITADIE THIS CLASS ANQWERE IN YMUR(PROGRAM. TE WRIPPEr�
# FU�CTION R}nWithYimldDelcq$HOLD(BE USED"AnSTEAT.
'-
�(Requirgl�XaramE�e�3:
# - indow m Vindow m the �in��w w(ich the ofject with yield d}lay kq%on.
`-(fuNc - functaon which ret5r.q a gmnerator of int � a nunctmon Uidh"a few�
# .ecessavy pargmeudrs wxich allow it to Sun gith"yieLd(fflay. A!`}nction needs#!to return a�generat�r of"inu. nee&{ a%yyend st!teieoq wi|h an inu whiCh 
# repreSents uhe fela9 (kn Milli{econ`s), and it .e%ds ` raise st�pIteretiof
# statemgnt a4 the enD of the fun#ioo�
#lass RunWithYieldDelqy:
 �  daf __iNit�(sedf, wi~dow, func)z
"    (` _�huck_typ�$wInfow, "win`n�2,!Wineo�)
0    "  �c`ec{_generatr func,"fwnc")�
!   
` ! c   selg._func`< gunc
    0$  s�lf_wkndow(= window
   (   0Sel�._ru~(9
 !"        
 �  � Rtarts the run wiuh"xield eelay.
    fa& _bun(seLf): 00     # this vkLl keep ruNlifg with yie�d de|A� until a StorHturatio� hs
!       #�rAised,$at w�ich point it0wmll s|oq 0      tzy:            delay = next(self._func)
            if delay is None:
                delay = 1000
        except StopIteration:
            delay = -1

        # update the window
        self._window._refresh()

        if delay >= 0:
            self._tag = self._window._root.after(delay, self._run)
        else:
            self._window._root.after_cancel(self._tag)
