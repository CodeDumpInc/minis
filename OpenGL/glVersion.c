//gcc ./glVersion.c -o ./glVersion -l glut

#include <stdio.h>
#include <GL/freeglut.h>

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);
	glutInitWindowSize(300, 300);
	glutInitDisplayMode( GLUT_RGB );
	glutCreateWindow("Context");
	
	GLchar* Names[] = {"Version", "Vendor", "GLSL Version", "Renderer"};
	GLuint Infos[] = {GL_VERSION, GL_VENDOR, 
			GL_SHADING_LANGUAGE_VERSION, GL_RENDERER};
	int count = 4;

	int i = 0;
	for(i=0; i < count; i++){
		char* version = (char*) glGetString(Infos[i]);

		printf("%s: %s\n", Names[i], version);
	}

	return 0;
}
