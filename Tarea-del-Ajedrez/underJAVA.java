//1. Esta clase representa una solucion en java a la funcion under de python
//2. Esto se hizo a modo de practica
//3. Este archivo cuenta como evidencia del desarrollo de la funcion para
//   apicarlo en python sea mas sencillo

//Autor:  Anthony Chaisa Fernandez
import java.util.ArrayList;
public class underJAVA{
    public static void main(String[] args) {
        //2 imagenes de ejemplo
        String[] square = {
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________",
            "__________________________________________________________"
        };
        String[] bishop = {
            "                                                          ",
            "                                                          ",
            "                                                          ",
            "                                                          ",
            "                            ##                            ",
            "                          ######                          ",
            "                         ###..###                         ",
            "                         ##....##                         ",
            "                         ##....##                         ",
            "                         ###..###                         ",
            "                          ######                          ",
            "                           ####                           ",
            "                         ########                         ",
            "                        ###....###                        ",
            "                      ####......####                      ",
            "                    ####..........####                    ",
            "                   ###..............###                   ",
            "                  ###................###                  ",
            "                 ###..................###                 ",
            "                ###.........##.........###                ",
            "                ##..........##..........##                ",
            "               ###..........##..........###               ",
            "               ##...........##...........##               ",
            "               ##.......##########.......##               ",
            "               ##.......##########.......##               ",
            "               ##...........##...........##               ",
            "               ##...........##...........##               ",
            "               ##...........##...........##               ",
            "               ###..........##..........###               ",
            "                ##..........##..........##                ",
            "                ###....................###                ",
            "                 ##....................###                ",
            "                 ###..................###                 ",
            "                  ###................###                  ",
            "                   ####################                   ",
            "                   ####################                   ",
            "                   ##................##                   ",
            "                  ###................###                  ",
            "                  ##..................##                  ",
            "                  ######################                  ",
            "                 ########################                 ",
            "                 ###..................###                 ",
            "                 #####..............#####                 ",
            "                 ########################                 ",
            "                      ##############                      ",
            "                          ######                          ",
            "                        ####..####                        ",
            "        ##################......##################        ",
            "      ##################..........##################      ",
            "    ####..........................................####    ",
            "    ###.....................##.....................###    ",
            "     ##...................######...................##     ",
            "     ###.########.......####  ####.......########.###     ",
            "      ####################      ####################      ",
            "       ##        #######          #######        ##       ",
            "                                                          ",
            "                                                          ",
            "                                                          "
        };
        
        //Creamos la nueva imagen (ArrayList)
        ArrayList<String> newImg = under(square, bishop);
        //Impresion
        imprimir(newImg);

    }

    public static ArrayList<String> under(String[] fondo, String[] frontal) {
        ArrayList<String> resultado = new ArrayList<>();
        //Limite
        int totalCaracteres = fondo.length * fondo[0].length();
        //Estos arreglos almacenaran los elementos individuales de toda la imagen
        String[] charFondo = new String[totalCaracteres];
        String[] charFrontal = new String[totalCaracteres];
        int aux = 0;
        //Este ciclo almacena lo indicado usando 'SUBSTRING' para cada linea
        for (int i = 0; i < fondo.length; i++) {
            for (int j = 0; j < fondo[i].length(); j++) {
                charFondo[aux] = fondo[i].substring(j, j + 1);
                charFrontal[aux] = frontal[i].substring(j, j + 1);
                aux++;
            }
        }
        //Variable que representa una linea, o un elemento de la imagen
        String line = "";
        //Comparando los elemento de los 2 arreglos
        //1. Si en la imagen frontal esta vacia (" ") en cierto indice,
        //   colocamos el elemento del fondo en ese mismo indice en la linea
        //   caso contrario, agregamos ese elemento del frontal en la linea
        //2. Se uso MODULOS para controlar las lineas y agragerlas como elemento en el nuevo arreglo
        for (int i = 0; i < totalCaracteres; i++) {
            if (charFrontal[i].equals(" ")) {
                if ((i + 1) % fondo.length != 0) {
                    line = line + charFondo[i];
                } else {
                    line = line + charFondo[i];
                    resultado.add(line);
                    line = "";
                }
            } else {
                if ((i + 1) % fondo.length != 0) {
                    line = line + charFrontal[i];
                } else {
                    line = line + charFrontal[i];
                    resultado.add(line);
                    line = "";
                }
            }
        }
        return resultado;
    }

    //METODO ROTATE
    public static ArrayList<String> rotate(String[] laImagen){
        //Resultado
        ArrayList<String> resultado = new ArrayList<>();
        //Considerando que la figura es igual de larga en cada linea
        //Caso contrario, seria otro for EXTERIOR que modifique en cada iteracion esa longitud
        int elementosLinea = laImagen[0].length();
        //elementos (lineas) en el dibujo
        int elementos = laImagen.length;
        String line = "";
        //Basicamente este ciclo recorre todos las lineas
        //de esa forma extraemos caracter por caracter
        for(int i = 0; i<elementosLinea;i++){
            for(int j = 0; j<elementos;j++){
                line += laImagen[j].substring(i, i+1);
            }
            //Agregamos esa linea
            resultado.add(line);
            //Reiniciamos la linea
            line = "";
        }
        return resultado;
    }
    //Metodo que imprime el arraylist
    public static void imprimir(ArrayList<String> img) {
        for (String linea : img) {
            System.out.println(linea);
        }
    }
}