## 🚩 PJT 05

### 🍀 이번 pjt를 통해 배운 내용
* 사용자 인증 기반 관계형 DB 설계
* CRUD 기능을 포함한 Web applicationw 제작

### 구현 중 오류를 통해 배운 점
* creating a modelform without either the 'fields' attribute or the 'exclude' attribute is prohibited; form customusercreationform needs updating.
  * UserCreationForm 클래스의 Meta 클래스를 불러와주지 않아서 발생했습니다.
  * class Meta(UserCreationForm):
      model = get_user_model() =>
    class Meta(UserCreationForm.Meta):
      model = get_user_model()

* reverse for 'update' with arguments '('',)' not found. 1 pattern(s) tried:
  * update로 전달해주는 인자에서 오타가 나서 발생했습니다
  * <a href="{% url 'movies:update' movie.pi %}">UPDATE</a><br> =>
    <a href="{% url 'movies:update' movie.pk %}">UPDATE</a><br>

* manager isn't available; 'auth.user' has been swapped for 'accounts.user'
  * 모델을 변경하고 마이그레이션을 해주지 않아서 발생했습니다.

* reverse for '<wsgirequest: get '/accounts/update/'>' not found. '<wsgirequest: get '/accounts/update/'>' is not a valid view function or pattern name.
 * render 대신 redirect로 작성했더니 발생했습니다
 * return redirect(request, 'accounts/update.html', context) =>
 return render(request, 'accounts/update.html', context)

 ### 후기
 무료 오픈소스 프레임워크로도  기능이 충분하고 완성도 있는 하나의 웹서비스를 만들어 낼 수 있다는게 놀랍다!
 개발자들이 프레임워크를 왜 적극적으로 활용하는지 배울 수 있었다 :-)
