import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")
folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True

workspace = arcpy.env.workspace
nr_planu = arcpy.GetParameterAsText(0)
sciezka = arcpy.GetParameterAsText(1)
fMz = arcpy.GetParameterAsText(2)
skala = arcpy.GetParameterAsText(3)
mpzpMap = aprx.listMaps("XXXX_MPZP")[0] 
mpzpLyt = aprx.listLayouts("XXXX_WYDRUK_MPZP")[0]
mpzpMap.name = "{}_MPZP".format(nr_planu)
mpzpLyt.name = f"{nr_planu}_WYDRUK_MPZP" 

mpzpMap = aprx.listMaps(f"{nr_planu}_MPZP")[0]

ptPodzwew = mpzpMap.listLayers("PUNKTY_PODZ_WEW")[0]
opDod = mpzpMap.listLayers("OPISY_DOD")[0]
ptSrodInf = mpzpMap.listLayers("PUNKTY_SROD_INFO")[0]
mz = mpzpMap.listLayers("MAPA_ZASADNICZA")[0]
przez = mpzpMap.listLayers("PRZEZ")[0]
przezUl = mpzpMap.listLayers("PRZEZ_ULICE")[0]
przezInfr = mpzpMap.listLayers("PRZEZ_INFR")[0]
przezKom = mpzpMap.listLayers("PRZEZ_KOM")[0]
rob = mpzpMap.listLayers("ROBOCZE")[0]
gran = mpzpMap.listLayers("GRANICA")[0]
punkty = mpzpMap.listLayers("PUNKTY")[0]
if "PRZEZ_MIX" in [layer.name for layer in mpzpMap.listLayers()]:
    przezMix = mpzpMap.listLayers("PRZEZ_MIX")[0]
else:
    pass

# ZAŁADOWANIE OPISÓW JEŚLI ISTNIEJĄ

if arcpy.Exists(r"{}\brg_mpzp.gdb\OPISY".format(sciezka)):
    arcpy.FeatureClassToFeatureClass_conversion(r"{}\brg_mpzp.gdb\OPISY".format(sciezka), workspace, "OPISY")
    op_przez = r"{}\OPISY".format(workspace)
    mpzpMap.addDataFromPath(op_przez)
    OpisyPrzez = mpzpMap.listLayers("OPISY")[0]
    cl = mpzpMap.listLayers("Class 1")[0]
    cl.name = "opisy_przeznaczenia"
elif arcpy.Exists(r"{}\brg_mpzp.gdb\opisy_przeznaczenia".format(sciezka)):
    arcpy.FeatureClassToFeatureClass_conversion(r"{}\brg_mpzp.gdb\opisy_przeznaczenia".format(sciezka), workspace, "OPISY")
    op_przez = r"{}\OPISY".format(workspace)
    mpzpMap.addDataFromPath(op_przez)
    OpisyPrzez = mpzpMap.listLayers("OPISY")[0]
    cl = mpzpMap.listLayers("Class 1")[0]
    cl.name = "opisy_przeznaczenia"
else:
    pass

# ZAŁADOWANIE WARSTW

if arcpy.Exists(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX".format(sciezka)):
    arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX".format(sciezka), r"{}\BRG_MPZP\PRZEZ_MIX".format(workspace), "TEST", r'GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,GlobalID,-1,-1;nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,nr_mpzp,0,10;nr_terenu "nr_terenu" true true false 3 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,nr_terenu,0,3;ozn_przezn "ozn_przezn" true true false 4 Long 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,ozn_przezn,-1,-1;przezn "przezn" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,przezn,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,pow,-1,-1;f2 "F2" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,f2,0,20;f3 "F3" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,f3,0,20;przezn_wyl "przezn_wyl" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,przezn_wyl,0,255;przezn_dop "przezn_dop" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,przezn_dop,0,255;przezn_szc "przezn_szc" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,przezn_szc,0,255;ulica "ulica" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,ulica,0,255;przekroj "przekroj" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,przekroj,0,255;tramwaj "tramwaj" true true false 3 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,tramwaj,0,3;chodnik "chodnik" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,chodnik,0,255;szer_ch_1 "szer_ch_1" true true false 4 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,szer_ch_1,-1,-1;szer_ch_2 "szer_ch_2" true true false 4 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,szer_ch_2,-1,-1;rower "rower" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,rower,0,255;parkowanie "parkowanie" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,parkowanie,0,255;szp_drzew "szp_drzew" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,szp_drzew,0,255;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,kod,0,4;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,Id,0,20;f1 "F1" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_MIX,f1,0,20', '', ''.format(sciezka))
else:
    pass

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\GRANICA".format(sciezka), r"{}\BRG_MPZP\GRANICA".format(workspace), "TEST", r'nazwa "nazwa" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,nazwa,0,255;dziel_urb "dziel_urb" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,dziel_urb,0,20;jedn_urban "jedn_urban" true true false 50 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,jedn_urban,0,50;autor "autor" true true false 50 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,autor,0,50;status "status" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,status,0,20;uchwala_P1 "uchwala_P1" true true false 30 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,uchwala_P1,0,30;data_P1 "data_P1" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_P1,-1,-1;uchwala_P2 "uchwala_P2" true true false 30 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,uchwala_P2,0,30;data_P2 "data_P2" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_P2,-1,-1;uchwala_P3 "uchwala_P3" true true false 30 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,uchwala_P3,0,30;data_P3 "data_P3" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_P3,-1,-1;wyl_1_pocz "wyl_1_pocz" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,wyl_1_pocz,-1,-1;wyl_1_kon "wyl_1_kon" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,wyl_1_kon,-1,-1;uchwala "uchwala" true true false 30 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,uchwala,0,30;data_uchwa "data_uchwa" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_uchwa,-1,-1;link_uchwa "link_uchwa" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,link_uchwa,0,255;nr_DzU "nr_DzU" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,nr_DzU,-1,-1;poz_DzU "poz_DzU" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,poz_DzU,-1,-1;data_DzU "data_DzU" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_DzU,-1,-1;link_DzU "link_DzU" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,link_DzU,0,255;uniew "uniew" true true false 50 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,uniew,0,50;typ_uniew "typ_uniew" true true false 50 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,typ_uniew,0,50;data_uniew "data_uniew" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,data_uniew,-1,-1;pow_mpzp "pow_mpzp" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,pow_mpzp,-1,-1;ukl_wsp "ukl_wsp" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,ukl_wsp,0,20;skala "skala" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,skala,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,Id,0,20;teryt "teryt" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,teryt,0,10;GlobalID "GlobalID" false false false 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,GlobalID,-1,-1;nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,nr_mpzp,0,10;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\GRANICA,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE".format(sciezka), r"{}\BRG_MPZP\INFO_DOD_LINIE".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,byt,0,255;typ_info "typ_info" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,typ_info,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_LINIE,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW".format(sciezka), r"{}\BRG_MPZP\INFO_DOD_POW".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,byt,0,255;typ_info "typ_info" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,typ_info,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,GlobalID,-1,-1;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,pow,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_POW,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY".format(sciezka), r"{}\BRG_MPZP\INFO_DOD_PUNKTY".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,byt,0,255;typ_info "typ_info" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,typ_info,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INFO_DOD_PUNKTY,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE".format(sciezka), r"{}\BRG_MPZP\INNE_GRANICE".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO".format(sciezka), r"{}\BRG_MPZP\INNE_GRANICE_INFO".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,nr_mpzp,0,10;byt "rodzaj_bytu" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,numer,0,10;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,etykieta,0,10;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,data_zrodl,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\INNE_GRANICE_INFO,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL".format(sciezka), r"{}\BRG_MPZP\LINIE_DKUL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_DKUL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR".format(sciezka), r"{}\BRG_MPZP\LINIE_INFR".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO".format(sciezka), r"{}\BRG_MPZP\LINIE_INFR_INFO".format(workspace), "TEST", r'GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,GlobalID,-1,-1;nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,numer,0,10;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,etykieta,0,10;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,data_zrodl,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,kod,0,4;id "id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_INFO,id,0,20', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL".format(sciezka), r"{}\BRG_MPZP\LINIE_INFR_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_INFR_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM".format(sciezka), r"{}\BRG_MPZP\LINIE_KOM".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,byt,0,255;szerokosc "szerokosc" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,szerokosc,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL".format(sciezka), r"{}\BRG_MPZP\LINIE_KOM_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,byt,0,255;szerokosc "szerokosc" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,szerokosc,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOM_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ".format(sciezka), r"{}\BRG_MPZP\LINIE_KOMPOZ".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL".format(sciezka), r"{}\BRG_MPZP\LINIE_KOMPOZ_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_KOMPOZ_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW".format(sciezka), r"{}\BRG_MPZP\LINIE_PODZ_WEW".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_PODZ_WEW,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG".format(sciezka), r"{}\BRG_MPZP\LINIE_REG".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,nr_mpzp,0,10;tolerancja "tolerancja" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,tolerancja,-1,-1;info_dod "info_dod" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,info_dod,0,20;info "info" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,info,0,255;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL".format(sciezka), r"{}\BRG_MPZP\LINIE_REG_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_REG_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR".format(sciezka), r"{}\BRG_MPZP\LINIE_ROZGR".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,nr_mpzp,0,10;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,kod,0,4;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR,byt,0,255', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD".format(sciezka), r"{}\BRG_MPZP\LINIE_SROD".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\LINIE_SROD,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD".format(sciezka), r"{}\BRG_MPZP\OPISY_DOD".format(workspace), "TEST", r'byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,byt,0,255;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,etykieta,0,10;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,kod,0,4;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,GlobalID,-1,-1;nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\OPISY_DOD,nr_mpzp,0,10', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB".format(sciezka), r"{}\BRG_MPZP\PARAM_I_FORMY_ZAB".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,nr_mpzp,0,10;nr_terenu "nr_terenu" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,nr_terenu,0,2;ozn_przezn "ozn_przezn" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,ozn_przezn,0,20;etykieta "etykieta" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,etykieta,0,2;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pow,-1,-1;udzF1_max "udzF1_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF1_max,-1,-1;udzF1_min "udzF1_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF1_min,-1,-1;udzF1_szac "udzF1_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF1_szac,-1,-1;udzF2_max "udzF2_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF2_max,-1,-1;udzF2_min "udzF2_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF2_min,-1,-1;udzF3_min "udzF3_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF3_min,-1,-1;udzF3_max "udzF3_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF3_max,-1,-1;udzF3_szac "udzF3_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF3_szac,-1,-1;fzF1 "fzF1" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,fzF1,0,255;fzF2 "fzF2" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,fzF2,0,255;fzF3 "fzF3" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,fzF3,0,255;dachF1 "dachF1" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,dachF1,0,255;dachF2 "dachF2" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,dachF2,0,255;dachF3 "dachF3" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,dachF3,0,255;pzF1_min "pzF1_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF1_min,-1,-1;pzF2_min "pzF2_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF2_min,-1,-1;pzF3_min "pzF3_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF3_min,-1,-1;pzF1_max "pzF1_max" true true false 0 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF1_max,-1,-1;pzF2_max "pzF2_max" true true false 0 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF2_max,-1,-1;pzF3_max "pzF3_max" true true false 0 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pzF3_max,-1,-1;pbF1_min "pbF1_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pbF1_min,-1,-1;pbF2_min "pbF2_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pbF2_min,-1,-1;pbF3_min "pbF3_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,pbF3_min,-1,-1;wzF1_min "wzF1_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF1_min,-1,-1;wzF2_min "wzF2_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF2_min,-1,-1;wzF3_min "wzF3_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF3_min,-1,-1;wzF1_max "wzF1_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF1_max,-1,-1;wzF2_max "wzF2_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF2_max,-1,-1;wzF3_max "wzF3_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,wzF3_max,-1,-1;kondF1_min "kondF1_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF1_min,-1,-1;kondF2_min "kondF2_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF2_min,-1,-1;kondF3_min "kondF3_min" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF3_min,-1,-1;kondF1_max "kondF1_max" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF1_max,-1,-1;kondF2_max "kondF2_max" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF2_max,-1,-1;kondF3_max "kondF3_max" true true false 2 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kondF3_max,-1,-1;intF1_min "intF1_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF1_min,-1,-1;intF2_min "intF2_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF2_min,-1,-1;intF3_min "intF3_min" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF3_min,-1,-1;intF1_max "intF1_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF1_max,-1,-1;intF2_max "intF2_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF2_max,-1,-1;intF3_max "intF3_max" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF3_max,-1,-1;intF1_szac "intF1_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF1_szac,-1,-1;intF2_szac "intF2_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF2_szac,-1,-1;intF3_szac "intF3_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,intF3_szac,-1,-1;zielen_min "zielen_min" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,zielen_min,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,GlobalID,-1,-1;udzF2_szac "udzF2_szac" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,udzF2_szac,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PARAM_I_FORMY_ZAB,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ".format(sciezka), r"{}\BRG_MPZP\PRZEZ".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,nr_mpzp,0,10;nr_terenu "nr_terenu" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,nr_terenu,0,2;przezn "przezn" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,przezn,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,pow,-1,-1;f1 "f1" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,f1,0,20;f2 "f2" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,f2,0,20;f3 "f3" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,f3,0,20;przezn_wyl "przezn_wyl" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,przezn_wyl,0,255;przezn_dop "przezn_dop" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,przezn_dop,0,255;przezn_szc "przezn_szc" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,przezn_szc,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,kod,0,4;ozn_przezn "ozn_przezn" true true false 4 Long 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ,ozn_przezn,-1,-1', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF".format(sciezka), r"{}\BRG_MPZP\PRZEZ_INF".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,nr_mpzp,0,10;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,GlobalID,-1,-1;przezn "przezn" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,przezn,0,255;nr_terenu "nr_terenu" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,nr_terenu,0,2;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,kod,0,4;ozn_przezn "ozn_przezn" true true false 4 Long 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_INF,ozn_przezn,-1,-1', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM".format(sciezka), r"{}\BRG_MPZP\PRZEZ_KOM".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,nr_mpzp,0,10;nr_terenu "nr_terenu" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,nr_terenu,0,2;ozn_przezn "ozn_przez" true true false 4 Long 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,ozn_przezn,-1,-1;przezn "przezn" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,przezn,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_KOM,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE".format(sciezka), r"{}\BRG_MPZP\PRZEZ_ULICE".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,nr_mpzp,0,10;nr_terenu "nr_terenu" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,nr_terenu,0,2;ozn_przezn "ozn_przez" true true false 0 Long 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,ozn_przezn,-1,-1;przezn "przezn" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,przezn,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,pow,-1,-1;przekroj "przekroj" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,przekroj,0,255;tramwaj "tramwaj" true true false 3 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,tramwaj,0,3;chodnik "chodnik" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,chodnik,0,255;szer_ch_1 "szer_ch_1" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,szer_ch_1,-1,-1;szer_ch_2 "szer_ch_2" true true false 0 Float 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,szer_ch_2,-1,-1;rower "rower" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,rower,0,255;parkowanie "parkowanie" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,parkowanie,0,255;szp_drzew "szp_drzew" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,szp_drzew,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,GlobalID,-1,-1;ulica "ulica" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,ulica,0,255;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PRZEZ_ULICE,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR".format(sciezka), r"{}\BRG_MPZP\PUNKTY_INFR".format(workspace), "TEST", r'byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR,byt,0,255;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR,GlobalID,-1,-1;nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR,nr_mpzp,0,10;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR,kod,0,4;id "id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR,id,0,20', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO".format(sciezka), r"{}\BRG_MPZP\PUNKTY_INFR_INFO".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,numer,0,10;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,etykieta,0,10;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,data_zrodl,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_INFO,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL".format(sciezka), r"{}\BRG_MPZP\PUNKTY_INFR_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_INFR_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ".format(sciezka), r"{}\BRG_MPZP\PUNKTY_KOMPOZ".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL".format(sciezka), r"{}\BRG_MPZP\PUNKTY_KOMPOZ_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_KOMPOZ_ZAL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW".format(sciezka), r"{}\BRG_MPZP\PUNKTY_PODZ_WEW".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,GlobalID,-1,-1;etykieta "etykieta" true true false 2 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,etykieta,0,2;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_PODZ_WEW,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG".format(sciezka), r"{}\BRG_MPZP\PUNKTY_REG".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_REG,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD".format(sciezka), r"{}\BRG_MPZP\PUNKTY_SROD".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,nr_mpzp,0,10;byt "kod" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,byt,0,255;gatunek "gatunek" true true false 50 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,gatunek,0,50;obwod "obwod" true true false 0 Short 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,obwod,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,Id,0,20;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,kod,0,4;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD,GlobalID,-1,-1', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO".format(sciezka), r"{}\BRG_MPZP\PUNKTY_SROD_INFO".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,numer,0,10;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,etykieta,0,10;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,data_zrodl,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\PUNKTY_SROD_INFO,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY".format(sciezka), r"{}\BRG_MPZP\STREFY".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,byt,0,255;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,Id,0,20;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,pow,-1,-1;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL".format(sciezka), r"{}\BRG_MPZP\STREFY_DKUL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,byt,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO".format(sciezka), r"{}\BRG_MPZP\STREFY_DKUL_INFO".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,numer,0,10;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,pow,-1,-1;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,data_zrodl,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_DKUL_INFO,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO".format(sciezka), r"{}\BRG_MPZP\STREFY_INFO".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,byt,0,255;numer "numer" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,numer,0,10;etykieta "etykieta" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,etykieta,0,10;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,pow,-1,-1;zrodlo "zrodlo" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,zrodlo,0,255;data_zrodl "data_zrodl" true true false 8 Date 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,data_zrodl,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_INFO,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD".format(sciezka), r"{}\BRG_MPZP\STREFY_SROD".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,byt,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD,kod,0,4', '', ''.format(sciezka))

arcpy.management.Append(r"{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL".format(sciezka), r"{}\BRG_MPZP\STREFY_SROD_ZAL".format(workspace), "TEST", r'nr_mpzp "nr_mpzp" true true false 10 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,nr_mpzp,0,10;byt "byt" true true false 255 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,byt,0,255;pow "pow" true true false 8 Double 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,pow,-1,-1;Id "Id" true true false 20 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,Id,0,20;GlobalID "GlobalID" false false true 38 GlobalID 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,GlobalID,-1,-1;kod "kod" true true false 4 Text 0 0,First,#,{}\brg_mpzp.gdb\BRG_MPZP\STREFY_SROD_ZAL,kod,0,4', '', ''.format(sciezka))

if arcpy.Exists(r"{}\brg_mpzp.gdb\OPISY".format(sciezka)) or arcpy.Exists(r"{}\brg_mpzp.gdb\opisy_przeznaczenia".format(sciezka)):
    przez.showLabels = False
    przezUl.showLabels = False
    przezInfr.showLabels = False
    przezKom.showLabels = False
    if "PRZEZ_MIX" in [layer.name for layer in mpzpMap.listLayers()]:
        przezMix.showLabels = False
    else:
        pass
else:
    pass

# ZAŁADOWANIE MAPY

pktMZ = mpzpMap.listLayers("PUNKTY")[1]
linMZ = mpzpMap.listLayers("LINIE")[1]

mapMZ = mpzpMap.listLayers("MAPA_ZASADNICZA")[0]

pktMzPath = (r"{}\{}_MZ_punkty.lpkx".format(fMz, nr_planu))
mpzpMap.addDataFromPath(pktMzPath)

linMzPath = (r"{}\{}_MZ_linie.lpkx".format(fMz, nr_planu))
mpzpMap.addDataFromPath(linMzPath)

if "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mpzpMap.listLayers()] and "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    budIurzP = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
elif "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mpzpMap.listLayers()]:
    budIurzL = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL.name = "BUDOWLE_I_URZADZENIA_1"
else:
    pass
if "BUDYNKI" in [lyr.name for lyr in mpzpMap.listLayers()] and "BUDYNKI_1" in [lyr.name for lyr in mpzpMap.listLayers()]:
    budP = mpzpMap.listLayers("BUDYNKI")[0]
    budL = mpzpMap.listLayers("BUDYNKI_1")[0]
elif "BUDYNKI" in [lyr.name for lyr in mpzpMap.listLayers()]:
    budL = mpzpMap.listLayers("BUDYNKI")[0]
    budL.name = "BUDYNKI_1"
else:
    pass
if "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewDzP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
elif "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewDzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL.name = "EWIDENCJA_GRUNTOW___DZIALKI_1"
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGrP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGrL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL.name = "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" 
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGoP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGoL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL.name = "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1"   
else:
    pass
if "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewUzP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
else:
    pass
if "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mpzpMap.listLayers()] and "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mpzpMap.listLayers()]:
    kItrP = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
elif "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mpzpMap.listLayers()]:
    kItrL = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL.name = "KOMUNIKACJA_I_TRANSPORT_1"
else:
    pass
if "OBIEKTY_INNE" in [layer.name for layer in mpzpMap.listLayers()] and "OBIEKTY_INNE_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oInP = mpzpMap.listLayers("OBIEKTY_INNE")[0]
    oInL = mpzpMap.listLayers("OBIEKTY_INNE_1")[0]
elif "OBIEKTY_INNE" in [layer.name for layer in mpzpMap.listLayers()]:
    oInL = mpzpMap.listLayers("OBIEKTY_INNE")[0]
    oInL.name = "OBIEKTY_INNE_1"
else:
    pass
if "OBSZAR_OPRACOWANIA" in [layer.name for layer in mpzpMap.listLayers()] and "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oOpP = mpzpMap.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL = mpzpMap.listLayers("OBSZAR_OPRACOWANIA_1")[0]
elif "OBSZAR_OPRACOWANIA" in [layer.name for layer in mpzpMap.listLayers()]:
    oOpL = mpzpMap.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL.name = "OBSZAR_OPRACOWANIA_1"
elif "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewUzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL.name = "EWIDENCJA_GRUNTOW___UZYTKI_1"
else:
    pass
if "OSNOWA" in [layer.name for layer in mpzpMap.listLayers()] and "OSNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    osP = mpzpMap.listLayers("OSNOWA")[0]
    osL = mpzpMap.listLayers("OSNOWA_1")[0]
elif "OSNOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    osL = mpzpMap.listLayers("OSNOWA")[0]
    osL.name = "OSNOWA_1"
else:
    pass
if "POKRYCIE_TERENU" in [layer.name for layer in mpzpMap.listLayers()] and "POKRYCIE_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    pTeP = mpzpMap.listLayers("POKRYCIE_TERENU")[0]
    pTeL = mpzpMap.listLayers("POKRYCIE_TERENU_1")[0]
elif "POKRYCIE_TERENU" in [layer.name for layer in mpzpMap.listLayers()]:
    pTeL = mpzpMap.listLayers("POKRYCIE_TERENU")[0]
    pTeL.name = "POKRYCIE_TERENU_1"
else:
    pass
if "RZEZBA_TERENU" in [layer.name for layer in mpzpMap.listLayers()] and "RZEZBA_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    rTeP = mpzpMap.listLayers("RZEZBA_TERENU")[0]
    rTeL = mpzpMap.listLayers("RZEZBA_TERENU_1")[0]
elif "RZEZBA_TERENU" in [layer.name for layer in mpzpMap.listLayers()]:
    rTeL = mpzpMap.listLayers("RZEZBA_TERENU")[0]
    rTeL.name = "RZEZBA_TERENU_1"
else:
    pass
if "SIATKA_KRZYZY" in [layer.name for layer in mpzpMap.listLayers()] and "SIATKA_KRZYZY_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKrP = mpzpMap.listLayers("SIATKA_KRZYZY")[0]
    sKrL = mpzpMap.listLayers("SIATKA_KRZYZY_1")[0]
elif "SIATKA_KRZYZY" in [layer.name for layer in mpzpMap.listLayers()]:
    sKrL = mpzpMap.listLayers("SIATKA_KRZYZY")[0]
    sKrL.name = "SIATKA_KRZYZY_1"
else:
    pass
if "SIEC_CIEPLOWNICZA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sCpP = mpzpMap.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL = mpzpMap.listLayers("SIEC_CIEPLOWNICZA_1")[0]
elif "SIEC_CIEPLOWNICZA" in [layer.name for layer in mpzpMap.listLayers()]:
    sCpL = mpzpMap.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL.name = "SIEC_CIEPLOWNICZA_1"
else:
    pass
if "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sElP = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
elif "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sElL = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL.name = "SIEC_ELEKTROENERGETYCZNA_1"
else:
    pass
if "SIEC_GAZOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_GAZOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sGaP = mpzpMap.listLayers("SIEC_GAZOWA")[0]
    sGaL = mpzpMap.listLayers("SIEC_GAZOWA_1")[0]
elif "SIEC_GAZOWA" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mpzpMap.listLayers("SIEC_GAZOWA")[0]
    sGaL.name = "SIEC_GAZOWA_1"
else:
    pass
if "SIEC_INNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_INNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sInP = mpzpMap.listLayers("SIEC_INNA")[0]
    sInL = mpzpMap.listLayers("SIEC_INNA_1")[0]
elif "SIEC_INNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sInL = mpzpMap.listLayers("SIEC_INNA")[0]
    sInL.name = "SIEC_INNA_1" 
else:
    pass
if "SIEC_KANALIZACYJNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKaP = mpzpMap.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL = mpzpMap.listLayers("SIEC_KANALIZACYJNA_1")[0]
elif "SIEC_KANALIZACYJNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sKaL = mpzpMap.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL.name = "SIEC_KANALIZACYJNA_1"
else:
    pass
if "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNiP = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
elif "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mpzpMap.listLayers()]:
    sNiL = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL.name = "SIEC_NIEZIDENTYFIKOWANA_1"
else:
    pass
if "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sTeP = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
elif "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sTeL = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL.name = "SIEC_TELEKOMUNIKACYJNA_1"
else:
    pass
if "SIEC_WODOCIAGOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sWoP = mpzpMap.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL = mpzpMap.listLayers("SIEC_WODOCIAGOWA_1")[0]
elif "SIEC_WODOCIAGOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sWoL = mpzpMap.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL.name = "SIEC_WODOCIAGOWA_1"
else:
    pass
if "SIEC_NAFTOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_NAFTOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNaP = mpzpMap.listLayers("SIEC_NAFTOWA")[0]
    sNaL = mpzpMap.listLayers("SIEC_NAFTOWA_1")[0]
elif "SIEC_NAFTOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sNaL = mpzpMap.listLayers("SIEC_NAFTOWA")[0]
    sNaL.name = "SIEC_NAFTOWA_1"
else:
    pass
if "SIEC_BENZYNOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_BENZYNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sBeP = mpzpMap.listLayers("SIEC_BENZYNOWA")[0]
    sBeL = mpzpMap.listLayers("SIEC_BENZYNOWA_1")[0]
elif "SIEC_BENZYNOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sBeL = mpzpMap.listLayers("SIEC_BENZYNOWA")[0]
    sBeL.name = "SIEC_BENZYNOWA_1"
else:
    pass

camera = aprx.activeView.camera
camera.setExtent(arcpy.Describe(ewDzL).extent)

try:
    if budIurzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budIurzL)
        mpzpMap.removeLayer(budIurzL)
    elif budIurzL.isFeatureLayer == False and budIurzP == True:
        mpzpMap.addLayerToGroup(linMZ, budIurzP)
        mpzpMap.removeLayer(budIurzP)
    else:
        arcpy.AddMessage("Brak warstwy budIurzL lub cos poszlo nie tak") 
except NameError:
    pass
try:
    if budIurzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, budIurzP)
        mpzpMap.removeLayer(budIurzP)
    else:
        arcpy.AddMessage("Brak warstwy budIurzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if budL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budL)
        mpzpMap.removeLayer(budL)
    elif budL.isFeatureLayer == False and budP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budP)
        mpzpMap.removeLayer(budP)
    else:
        arcpy.AddMessage("Brak warstwy budL lub cos poszlo nie tak")  
except NameError:
    pass
try:
    if budP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, budP)
        mpzpMap.removeLayer(budP)
    else:
        arcpy.AddMessage("Brak warstwy budP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewDzL)
        mpzpMap.removeLayer(ewDzL)
    elif ewDzL.isFeatureLayer == False and ewDzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewDzP)
        mpzpMap.removeLayer(ewDzP)
    else:
        arcpy.AddMessage("Brak warstwy ewDzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewDzP)
        mpzpMap.removeLayer(ewDzP)
    else:
        arcpy.AddMessage("Brak warstwy ewDzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGrL)
        mpzpMap.removeLayer(ewGrL)
    elif ewGrL.isFeatureLayer == False and ewGrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGrP)
        mpzpMap.removeLayer(ewGrP)
    else:
        arcpy.AddMessage("Brak warstwy ewGrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewGrP)
        mpzpMap.removeLayer(ewGrP)
    else:
        arcpy.AddMessage("Brak warstwy ewGrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGoL)
        mpzpMap.removeLayer(ewGoL)
    elif ewGoL.isFeatureLayer == False and ewGoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGoP)
        mpzpMap.removeLayer(ewGoP)
    else:
        arcpy.AddMessage("Brak warstwy ewGoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewGoP)
        mpzpMap.removeLayer(ewGoP)
    else:
        arcpy.AddMessage("Brak warstwy ewGoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewUzL)
        mpzpMap.removeLayer(ewUzL)
    elif ewUzL.isFeatureLayer == False and ewUzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewUzP)
        mpzpMap.removeLayer(ewUzP)
    else:
        arcpy.AddMessage("Brak warstwy ewUzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewUzP)
        mpzpMap.removeLayer(ewUzP)
    else:
        arcpy.AddMessage("Brak warstwy ewUzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, kItrL)
        mpzpMap.removeLayer(kItrL)
    elif kItrL.isFeatureLayer == False and kItrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, kItrP)
        mpzpMap.removeLayer(kItrP)
    else:
        arcpy.AddMessage("Brak warstwy kItrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, kItrP)
        mpzpMap.removeLayer(kItrP)
    else:
        arcpy.AddMessage("Brak warstwy kItrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oInL)
        mpzpMap.removeLayer(oInL)
    elif oInL.isFeatureLayer == False and oInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oInP)
        mpzpMap.removeLayer(oInP)
    else:
        arcpy.AddMessage("Brak warstwy oInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, oInP)
        mpzpMap.removeLayer(oInP)
    else:
        arcpy.AddMessage("Brak warstwy oInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oOpL)
        mpzpMap.removeLayer(oOpL)
    elif oOpL.isFeatureLayer == False and oOpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oOpP)
        mpzpMap.removeLayer(oOpP)
    else:
        arcpy.AddMessage("Brak warstwy oOpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, oOpP)
        mpzpMap.removeLayer(oOpP)
    else:
        arcpy.AddMessage("Brak warstwy oOpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, osL)
        mpzpMap.removeLayer(osL)
    elif osL.isFeatureLayer == False and osP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, osP)
        mpzpMap.removeLayer(osP)
    else:
        arcpy.AddMessage("Brak warstwy osL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, osP)
        mpzpMap.removeLayer(osP)
    else:
        arcpy.AddMessage("Brak warstwy osP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, pTeL)
        mpzpMap.removeLayer(pTeL)
    elif pTeL.isFeatureLayer == False and pTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, pTeP)
        mpzpMap.removeLayer(pTeP)
    else:
        arcpy.AddMessage("Brak warstwy pTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, pTeP)
        mpzpMap.removeLayer(pTeP)
    else:
        arcpy.AddMessage("Brak warstwy pTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, rTeL)
        mpzpMap.removeLayer(rTeL)
    elif rTeL.isFeatureLayer == False and rTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, rTeP)
        mpzpMap.removeLayer(rTeP)
    else:
        arcpy.AddMessage("Brak warstwy rTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, rTeP)
        mpzpMap.removeLayer(rTeP)
    else:
        arcpy.AddMessage("Brak warstwy rTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKrL)
        mpzpMap.removeLayer(sKrL)
    elif sKrL.isFeatureLayer == False and sKrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKrP)
        mpzpMap.removeLayer(sKrP)
    else:
        arcpy.AddMessage("Brak warstwy sKrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sKrP)
        mpzpMap.removeLayer(sKrP)
    else:
        arcpy.AddMessage("Brak warstwy sKrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sCpL)
        mpzpMap.removeLayer(sCpL)
    elif sCpL.isFeatureLayer == False and sCpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sCpP)
        mpzpMap.removeLayer(sCpP)
    else:
        arcpy.AddMessage("Brak warstwy sCpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sCpP)
        mpzpMap.removeLayer(sCpP)
    else:
        arcpy.AddMessage("Brak warstwy sCpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sElL)
        mpzpMap.removeLayer(sElL)
    elif sElL.isFeatureLayer == False and sElP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sElP)
        mpzpMap.removeLayer(sElP)
    else:
        arcpy.AddMessage("Brak warstwy sElL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sElP)
        mpzpMap.removeLayer(sElP)
    else:
        arcpy.AddMessage("Brak warstwy sElP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sGaL)
        mpzpMap.removeLayer(sGaL)
    elif sGaL.isFeatureLayer == False and sGaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sGaP)
        mpzpMap.removeLayer(sGaP)
    else:
        arcpy.AddMessage("Brak warstwy sGaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sGaP)
        mpzpMap.removeLayer(sGaP)
    else:
        arcpy.AddMessage("Brak warstwy sGaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sInL)
        mpzpMap.removeLayer(sInL)
    elif sInL.isFeatureLayer == False and sInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sInP)
        mpzpMap.removeLayer(sInP)
    else:
        arcpy.AddMessage("Brak warstwy sInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sInP)
        mpzpMap.removeLayer(sInP)
    else:
        arcpy.AddMessage("Brak warstwy sInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKaL)
        mpzpMap.removeLayer(sKaL)
    elif sKaL.isFeatureLayer == False and sKaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKaP)
        mpzpMap.removeLayer(sKaP)
    else:
        arcpy.AddMessage("Brak warstwy sKaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sKaP)
        mpzpMap.removeLayer(sKaP)
    else:
        arcpy.AddMessage("Brak warstwy sKaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNiL)
        mpzpMap.removeLayer(sNiL)
    elif sNiL.isFeatureLayer == False and sNiP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNiP)
        mpzpMap.removeLayer(sNiP)
    else:
        arcpy.AddMessage("Brak warstwy sNiL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sNiP)
        mpzpMap.removeLayer(sNiP)
    else:
        arcpy.AddMessage("Brak warstwy sNiP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sTeL)
        mpzpMap.removeLayer(sTeL)
    elif sTeL.isFeatureLayer == False and sTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sTeP)
        mpzpMap.removeLayer(sTeP)
    else:
        arcpy.AddMessage("Brak warstwy sTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sTeP)
        mpzpMap.removeLayer(sTeP)
    else:
        arcpy.AddMessage("Brak warstwy sTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sWoL)
        mpzpMap.removeLayer(sWoL)
    elif sWoL.isFeatureLayer == False and sWoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sWoP)
        mpzpMap.removeLayer(sWoP)
    else:
        arcpy.AddMessage("Brak warstwy sWoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sWoP)
        mpzpMap.removeLayer(sWoP)
    else:
        arcpy.AddMessage("Brak warstwy sWoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNaL)
        mpzpMap.removeLayer(sNaL)
    elif sNaL.isFeatureLayer == False and sNaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNaP)
        mpzpMap.removeLayer(sNaP)
    else:
        arcpy.AddMessage("Brak warstwy sNaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sNaP)
        mpzpMap.removeLayer(sNaP)
    else:
        arcpy.AddMessage("Brak warstwy sNaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sBeL)
        mpzpMap.removeLayer(sBeL)
    elif sBeL.isFeatureLayer == False and sBeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sBeP)
        mpzpMap.removeLayer(sBeP)
    else:
        arcpy.AddMessage("Brak warstwy sBeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sBeP)
        mpzpMap.removeLayer(sBeP)
    else:
        arcpy.AddMessage("Brak warstwy sBeP lub cos poszlo nie tak")
except NameError:
    pass

pktMZ.name = "PUNKTY_MZ"
linMZ.name = "LINIE_MZ"

pktMZ = mpzpMap.listLayers("PUNKTY_MZ")[0]
linMZ = mpzpMap.listLayers("LINIE_MZ")[0]

rasMzPath = (r"{}\PODKLAD_{}.tif".format(fMz, nr_planu))
mpzpMap.addDataFromPath(rasMzPath)
rasMz = mpzpMap.listLayers(f"PODKLAD_{nr_planu}.tif")[0]
rasMz.name = f"PODKLAD_{nr_planu}"

arcpy.management.DefineProjection(rasMz, 'PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

powLyr = mpzpMap.listLayers("POWIERZCHNIE")[0]

mpzpMap.moveLayer(powLyr, rasMz, "AFTER")

rasMz.visible = False


arcpy.AddMessage(nr_planu)

arcpy.AddMessage(sciezka)

arcpy.AddMessage(fMz)

arcpy.AddMessage(skala)

arcpy.AddMessage("Brawo - mapa podgrana i przeladowane warstwy")

arcpy.AddMessage("Brawo - mapa zasadnicza w formie rastrowej i wektorowej zaladowana")

arcpy.AddMessage("Brawo! Elegancko zamienione etykiety na opisy")



